from groq import Groq

client = Groq(api_key="ENTER_KEY_HERE")

def call_llm(messages):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content
