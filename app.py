import streamlit as st
from agent import AgentManager

st.set_page_config(page_title="AI Customer Support", layout="wide")

st.title("🤖 Multi-Agent Customer Support")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

manager = AgentManager()

# Clear chat
col1, col2 = st.columns([8, 1])
with col2:
    if st.button("🗑️"):
        st.session_state.chat_history = []
        st.rerun()

# Input
user_input = st.chat_input("Ask your question...")

if user_input:
    # Add user message immediately
    st.session_state.chat_history.append({
        "role": "user",
        "message": user_input
    })

    #  Spinner while processing
    with st.spinner("🤖 Thinking..."):
        result = manager.handle_query(user_input, st.session_state.chat_history)

    # Add bot response after thinking
    st.session_state.chat_history.append({
        "role": "bot",
        "message": result["response"],
        "agent": result["agent"]
    })

# Badge colors
color_map = {
    "REFUND": "#1f77b4",
    "SHIPPING": "#2ca02c",
    "TECHNICAL": "#ff7f0e",
    "ESCALATION": "#d62728"
}

# Display chat
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        with st.chat_message("user"):
            st.markdown(chat["message"])
    else:
        with st.chat_message("assistant"):
            agent = chat.get("agent", "BOT")
            color = color_map.get(agent, "#444")

            badge = f"""
            <span style='background-color:{color};
                         padding:4px 10px;
                         border-radius:10px;
                         color:white;
                         font-size:12px;'>
            🤖 {agent}
            </span>
            """

            st.markdown(badge, unsafe_allow_html=True)
            st.markdown(chat["message"])

st.markdown("---")
st.caption("Groq LLM • RAG • Tool Calling • Agent Loop • Memory")