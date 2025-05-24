import os
from dotenv import load_dotenv
import pandas as pd

from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# Load environment variables from .env file
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

# read csv file
df = pd.read_csv("./data/salaries_2023.csv").fillna(value=0)

# Initialize the model
llm = ChatOpenAI(
    api_key=openai_key,
    model="gpt-4o-mini",
    temperature=0,
)

# Create a pandas agent using function-calling
agent = create_pandas_dataframe_agent(
    llm=llm,
    df=df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS
)

# Ask a question using the correct column name
response = agent.invoke("find total distinct department names?")
print(response["output"])
