from langchain.schema import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st

# Load environment variables from .env file
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

llm_name = "gpt-4o-mini"
model = ChatOpenAI(api_key=openai_key, model=llm_name)
BEHAVE_AS = "You are a helpful assistant who is extremely competent "
"as a Computer Scientist! Your name is Rob."

def first_agent(message):
    res = model.invoke(message)
    return res


def run_agent():
    print("Simple AI Agent: Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print("...")
        message = [SystemMessage(content=BEHAVE_AS), HumanMessage(content=user_input)]
        response = first_agent(message)
        print(f"AI Agent: {response.content}")


if __name__ == "__main__":
    run_agent()