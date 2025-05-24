import os
from dotenv import load_dotenv

import streamlit as st
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

st.title("AI Agent with LangChain")

if not openai_key:
    st.error("Missing OpenAI API Key. Please set OPENAI_API_KEY in your .env file.")
    st.stop()

def load_model():
    return ChatOpenAI(api_key=openai_key, model="gpt-4o-mini")

model = load_model()
BEHAVE_AS = "You are a helpful assistant who is extremely competent as a Computer Scientist! Your name is Rob."

question = st.text_input("### Ask a Question", "")

if question:
    with st.spinner("Thinking ..."):
        messages = [
            SystemMessage(content=BEHAVE_AS),
            HumanMessage(content=question),
        ]
        answer = model.invoke(messages)
        st.write("## Final Answer")
        st.markdown(answer.content)