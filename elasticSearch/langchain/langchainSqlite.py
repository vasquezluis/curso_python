import sqlite3
import os
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain.sql_database import SQLDatabase

os.environ['OPENAI_API_KEY'] = ""

# get the db
db = SQLDatabase.from_uri("sqlite:///./Chinook.db")
toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))

agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True,
    anget_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# example
agent_executor.run("What is the most repeated Genre in the Track table and how many?")
