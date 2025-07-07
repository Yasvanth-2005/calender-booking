import streamlit as st
import requests
import re


st.set_page_config(page_title="📅 Calendar Booking Assistant")
st.title("📅 Calendar Booking Assistant")


backend_url = "https://calender-booking-2w76.onrender.com/chat"
# backend_url = "http://127.0.0.1:8000/chat"


def normalize_prompt(text):
    text = re.sub(r"[‘’]", "'", text)
    text = re.sub(r'[“”]', '"', text)
    return text.strip()

if 'messages' not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask to book an appointment...")

if user_input:
    clean_input = normalize_prompt(user_input)
    st.session_state.messages.append({"role": "user", "content": clean_input})

    try:
        response = requests.post(backend_url, json={"message": clean_input})
        response.raise_for_status()
        response_data = response.json()
        reply = response_data.get("response", "⚠️ No 'response' key in API reply.")
    except requests.exceptions.RequestException as e:
        reply = f"⚠️ Request failed: {e}"
    except ValueError:
        reply = f"⚠️ Failed to parse response as JSON. Raw response:\n\n{response.text}"
    except Exception as e:
        reply = f"⚠️ Unexpected error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": reply})


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
