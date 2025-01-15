import streamlit as st
from transformer import TransformerModel
from dotenv import load_dotenv
import os

# luam api key din dotenv
def get_api_key() -> str:
    load_dotenv()
    return os.getenv("OPENAI_SECRET_API_KEY")

api_key = get_api_key()
if not api_key:
    st.error("OpenAI API key is missing. Please add it to the dotenv file.")
    st.stop()

# initializam modelul
transformer = TransformerModel(api_key)

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# headers
st.title("Transformer Chatbot with History")
st.write("Chat with GPT and keep track of your conversation!")

# afisam istoricul chatului
for message in st.session_state["messages"]:
    role = "user" if message["role"] == "user" else "assistant"
    st.chat_message(role).write(message["content"])

# inputul chatului
user_input = st.chat_input("Ask something...")
if user_input:
    st.chat_message("user").write(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})

    with st.spinner("Generating response..."):
        response = transformer.generate_response(st.session_state["messages"])
        st.session_state["messages"].append({"role": "assistant", "content": response})

    st.chat_message("assistant").write(response)