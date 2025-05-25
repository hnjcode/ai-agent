import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# Load environment variables from .env file
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

# llm_name = "gpt-3.5-turbo"
llm_name = "gpt-4o-mini"
model = ChatOpenAI(api_key=openai_key, model=llm_name)

db_config = {
    "host": "localhost",
    "port": 3307,
    "user": "root",
    "password": "1111",
    "database": "ai_agent_db"
}

# Create the connection string
conn_str = (
    f"mysql+pymysql://{db_config['user']}:{db_config['password']}"
    f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
)

from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri(conn_str)
toolkit = SQLDatabaseToolkit(db=db, llm=model)

QUESTION = "confirm salaries table exist in database ?"

# [IMPORTANT] these questions may exceed the token limit of gpt-4o-mini model
# QUESTION = "what is the highest average salary by department, and give me the number?"
# QUESTION = "what is the average base_salary from salaries table?"

sql_agent = create_sql_agent(
    llm=model,
    toolkit=toolkit,
    top_k=5,
    verbose=True,
)

res = sql_agent.invoke({"input": QUESTION})
print(res["output"])

