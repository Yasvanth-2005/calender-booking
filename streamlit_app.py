import streamlit as st
import requests
import re


st.set_page_config(page_title="📅 Calendar Booking Assistant")
st.title("📅 Calendar Booking Assistant")


backend_url = "https://calender-booking-2w76.onrender.com/chat"
# backend_url = "http://127.0.0.1:8000/chat"


if 'messages' not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask to book an appointment...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    try:
        response = requests.post(backend_url, json={"message": user_input})
        response.raise_for_status()
        reply = response.json().get("response") or "No reply"
    except Exception as e:
        reply = f"⚠️ Error: {str(e)}"
    
    st.session_state.messages.append({"role": "assistant", "content": reply})

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])