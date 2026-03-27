from llm import call_llm
from rag import retrieve
from tools import TOOLS
import config


# ---------------- ROUTER ----------------
class RouterAgent:
    def classify(self, query):
        messages = [
            {"role": "system", "content": config.SYSTEM_PROMPTS["ROUTER"]},
            {"role": "user", "content": query}
        ]
        return call_llm(messages).strip().upper()


# ---------------- TOOL AGENT ----------------
class ToolAgent:
    def __init__(self, category):
        self.category = category

    def handle(self, query, history=None):
        context = "\n".join(retrieve(query))

        messages = [
            {
                "role": "system",
                "content": f"""
You are a {self.category} customer support agent.

GENERAL RULES:
- Be friendly and helpful
- Never show tool calls
- Never include 'TOOL:' in final answer
- Keep answers clear and structured

------------------------

IF CATEGORY = REFUND:
- Explain refund policy clearly
- Mention 30-day rule if relevant
- Give step-by-step refund process
- Be polite and reassuring

Example style:
"You're eligible for a refund 
Here is what you can do:
1. Go to your orders
2. Select the product
3. Click 'Request Refund'"

------------------------

IF CATEGORY = SHIPPING:
- Provide delivery timelines
- Mention standard (5 to 7 days) or express (1 to 2 days)
- Reassure customer if delayed
- Suggest tracking if needed

Example style:
"Your order is on the way 
Standard delivery takes 5 to 7 days..."

------------------------

IF CATEGORY = TECHNICAL:
- Always give step-by-step instructions
- Keep it simple
- Never ask for passwords
- Help user recover access

Example style:
"No worries, here is how to fix it:
1. Click 'Forgot Password'
2. Enter your email..."

------------------------

PROCESS:
1. Understand the query
2. Decide if tool is needed
3. If needed respond EXACTLY:
   TOOL: tool_name
4. After tool result, give final answer

Available tools:
{list(TOOLS.keys())}

Context:
{context}
"""
            }
        ]
        
        # -------- MEMORY --------
        if history:
            for h in history[-4:]:
                messages.append({
                    "role": "user" if h["role"] == "user" else "assistant",
                    "content": h["message"]
                })

        messages.append({"role": "user", "content": query})

        # -------- AGENT LOOP --------
        for _ in range(3):
            response = call_llm(messages)

            # -------- TOOL CALL DETECT --------
            if "TOOL:" in response:
                tool_name = response.split("TOOL:")[-1].strip()

                if tool_name in TOOLS:
                    tool_result = TOOLS[tool_name]()

                    # Hide tool step from user
                    messages.append({
                        "role": "assistant",
                        "content": f"(Used tool: {tool_name})"
                    })

                    messages.append({
                        "role": "user",
                        "content": f"""
Tool result: {tool_result}

Now generate the FINAL answer for the user.
DO NOT mention tools.
DO NOT include TOOL.
Just give a clean helpful answer.
"""
                    })

                    continue

            # -------- FINAL CLEAN RESPONSE --------
            clean_response = response.replace("TOOL:", "").strip()
            return clean_response

        return "Sorry, I couldn't fully resolve your request."


# ---------------- AGENT MANAGER ----------------
class AgentManager:
    def __init__(self):
        self.router = RouterAgent()
        self.agents = {
            "REFUND": ToolAgent("REFUND"),
            "SHIPPING": ToolAgent("SHIPPING"),
            "TECHNICAL": ToolAgent("TECHNICAL")
        }

    def handle_query(self, query, history=None):
        # Escalation case
        if query.isupper():
            return {
                "agent": "ESCALATION",
                "response": "Your issue has been escalated to human support."
            }

        category = self.router.classify(query)

        if category not in self.agents:
            return {
                "agent": "ESCALATION",
                "response": "Could not classify your request."
            }

        response = self.agents[category].handle(query, history)

        return {
            "agent": category,
            "response": response
        }