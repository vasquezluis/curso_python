from rest_framework.response import Response
from rest_framework.decorators import api_view

import os

# chat
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
  ChatPromptTemplate,
  HumanMessagePromptTemplate,
  MessagesPlaceholder,
  SystemMessagePromptTemplate
)

# csv
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI 
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

# sqlite
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.sql_database import SQLDatabase

# mysql
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.sql_database import SQLDatabase

os.environ['OPENAI_API_KEY'] = ""

# chain_chat function
prompt = ChatPromptTemplate.from_messages(
  [
    SystemMessagePromptTemplate.from_template(
      "Your a friendly chat assistant. You responde to the user's messages and ask questions to keep the conversation going."
    ),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}"),
  ]
)
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

# csv_chat function
agent = create_csv_agent(
    OpenAI(temperature=0),
    "static/datosMotos.csv",
    verbose=True,
    anget_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# sqlite_chat function
db = SQLDatabase.from_uri("sqlite:///static/Chinook.db")
toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))
agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True,
    anget_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# mysql_chat function

# CHAT endpoint
@api_view(['POST'])
def chat(request):
  response = conversation.run(input = request.data.get('message'))

  return Response({'message': 'langchain response', 'body': response})
  
# CSV endpoint
@api_view(['POST'])
def langchainCSV(request):

  question = request.data.get('message')
  print('question: ', question)
  
  try:
    response = agent.run(question)
    print('response: ', response)
  except Exception as e:
    response = str(e)
    print('error: ', response)
  
  return Response({'message': 'langchain response', 'body': response})

# SQLITE endpoint
@api_view(['POST'])
def langchainSqlite(request):

  question = request.data.get('message')
  print('question: ', question)
  
  try:
    response = agent_executor.run(question)
    print('response: ', response)
  except Exception as e:
    response = str(e)
    print('error: ', response)
  
  return Response({'message': 'langchain response', 'body': response})

# MYSQL endpoint
# @api_view(['POST'])
# def langchainmysql(request):

