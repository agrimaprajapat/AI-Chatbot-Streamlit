from dotenv import load_dotenv 
load_dotenv() 

import streamlit as st 
import os 
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash") 

def my_output(query):
    response = model.generate_content(query) 
    return response.text 

#### UI Development using streamlit 

import streamlit as st

st.set_page_config(page_title="SMART_BOT", page_icon="🤖")

st.title("🤖 SMART_BOT")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = my_output(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)