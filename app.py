
import streamlit as st
from langchain_ollama import OllamaLLM

st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 My AI Chatbot")
st.caption("Powered by LangChain + Ollama")

# Load local LLM
@st.cache_resource
def load_model():
    return OllamaLLM(model="llama3.1:8b")

model = load_model()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("Ask me anything..."):

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Build conversation history
    history = ""

    for message in st.session_state.messages:
        role = "User" if message["role"] == "user" else "Assistant"
        history += f"{role}: {message['content']}\n"

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    full_prompt = f"""
You are a helpful AI assistant.

Previous conversation:
{history}

User: {prompt}
Assistant:
"""

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("AI is thinking..."):
            try:
                response = model.invoke(full_prompt)
                st.markdown(response)

                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )

            except Exception as e:
                st.error(f"Error connecting to Ollama: {e}")
