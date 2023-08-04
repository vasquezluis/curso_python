import os
from langchain.agents import create_csv_agent

from langchain.llms import OpenAI 
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

os.environ['OPENAI_API_KEY'] = "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"

# config
#agent = create_csv_agent(
#    OpenAI(temperature=0),
#    "https://drive.google.com/file/d/12Lqkr99-etYXv2PbnHOMPSbQ0ixEglDj/view?usp=drive_link",
#    verbose=True,
#    anget_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
#)

agent = create_csv_agent(
    OpenAI(temperature=0),
    "datosMotos.csv",
    verbose=True,
    anget_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# example
agent.run("cuantos tipos de linea de productos hay?")
