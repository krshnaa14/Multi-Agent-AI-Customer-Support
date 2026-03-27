## Multi-Agent AI Customer Support System
# 🚀 Project Overview

This project is a multi-agent AI customer support system built using Groq LLM, RAG-based retrieval, and tool-calling agents. It simulates a professional customer support environment where queries are automatically routed to specialized agents, processed with reasoning, and responded to with relevant knowledge or actions.

# Key Features:

Multi-agent architecture: REFUND, SHIPPING, TECHNICAL, GENERAL agents

Retrieval-Augmented Generation (RAG) for knowledge-based responses

Tool-calling for actions like checking orders, processing refunds, or escalating issues

Stateful chat with memory and context tracking

Streamlit UI with loading spinner and agent badges

Escalation handling for angry or complex customer queries

# 🏗 Architecture
User Input → Router Agent → Specialized Agent → Tool Calls → RAG Retrieval → LLM Response → Streamlit UI

# 📦 File Structure

app.py	(Streamlit frontend with chat interface)

agent.py	(Multi-agent system logic, routing, tool-calling, agent loop)

llm.py	(Groq LLM wrapper for chat completions)

tools.py	(Mock tools: order tracking, refunds, account info, escalations)

config.py	(System prompts, tool definitions, and constants)

test.py	(Test cases for agent responses and metrics)

requirements.txt	(Python dependencies)

README.md	(Project documentation)

# 🔑 API Key Setup

This project uses Groq LLM, which requires an API key. Follow these steps to create and configure it:

1. Sign up / Log in to Groq 
Go to Groq Console
Sign up or log in with your account
2. Create an API Key
Navigate to API Keys in your dashboard
Click Create New Key
Give it a name (e.g., multi-agent-support)
Copy the generated key — you’ll use it in the next step

⚠️ Keep this key private. Do not share it publicly.

# 💡 How It Works

Router Agent: Classifies queries into categories (REFUND, SHIPPING, TECHNICAL, GENERAL).

Specialized Agents: Each agent handles domain-specific queries and has its own system prompt for style and context.

Tool Calling: Agents call mock tools to fetch order info, check refund eligibility, or escalate issues.

RAG (Retrieval-Augmented Generation): Agents retrieve relevant knowledge base documents for informed responses.

Memory / Chat History: Maintains conversation context and allows follow-up queries to make sense of pronouns like “it” or “that order.”

Streamlit UI: Interactive interface with agent badges, loading spinner, and “Clear Chat” functionality.


# 🏷 Key Learnings
Implementing multi-agent systems in Python
Routing user queries intelligently with LLMs
Using RAG (FAISS) for context-aware responses
Building tool-calling agents to simulate real-world actions
Maintaining chat history and conversational memory
Creating an interactive Streamlit interface for AI applications
Handling escalations and complex customer scenarios


# 📈 Testing

Run test.py to verify agent responses, tool calls, and metrics:

python test.py
Tracks:
Total queries
Resolved without escalation
Escalations
Average tool calls per query
Response time

# 💡 Pro Tips

Always test follow-up questions to check memory context

Check tool calling logs to debug agent reasoning

Observe agent badges in UI to confirm correct routing
