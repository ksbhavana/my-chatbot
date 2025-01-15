import streamlit as st
from chatbot_logic import handle_user_input

st.title("GreenLife Foods Chatbot")

user_input = st.text_input("How can I assist you today?")
if st.button("Send"):
    response = handle_user_input(user_input)
    st.write(f"Bot: {response}")
