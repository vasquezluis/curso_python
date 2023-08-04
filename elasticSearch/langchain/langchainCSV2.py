import os
import gdown # for download google drive file
from langchain.agents import create_csv_agent 
from langchain.llms import OpenAI 
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

os.environ['OPENAI_API_KEY'] = ""

# download the google drive file and store it locally
file_url = "https://drive.google.com/file/d/12Lqkr99-etYXv2PbnHOMPSbQ0ixEglDj/view?usp=drive_link",
file_path = "./datosMotosGD.csv" # file path/name
gdown.download(file_url, file_path)

agent = create_csv_agent(
    OpenAI(temperature=0),
    file_path,
    verbose=True,
    anget_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# example
agent.run("cuantos tipos de linea de productos hay?")
