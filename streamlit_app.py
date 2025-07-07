import streamlit as st
import requests

st.set_page_config(page_title="Calendar Booking Assistant")
st.title("📅 Calendar Booking Assistant")

backend_url = "https://your-fastapi-url/chat" 

if 'messages' not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask to book an appointment...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = requests.post(backend_url, json={"message": user_input})
    reply = response.json()["reply"]
    st.session_state.messages.append({"role": "assistant", "content": reply})

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
