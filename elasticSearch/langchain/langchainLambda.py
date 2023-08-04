import os
import tempfile
import boto3
import gdown
from langchain.agents import create_agent_csv
from langchain.llms import OpenAI
from langchain.agents.agent_types import AgentType

def lambda_handler(event, context):
    # Set the OpenAI API key
    os.environ['OPENAI_API_KEY'] = "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"

    # Download the file from Google Drive and save it to a temporary location
    file_url = "https://drive.google.com/uc?id=12Lqkr99-etYXv2PbnHOMPSbQ0ixEglDj"
    with tempfile.NamedTemporaryFile() as temp_file:
        file_path = temp_file.name
        gdown.download(file_url, file_path)

        # Create the agent with the local file path
        agent = create_agent_csv(
            OpenAI(temperature=0),
            file_path,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
        )

        # Example usage
        response = agent.run("cuantos tipos de linea de productos hay?")
        
        # Return the response
        return {
            'statusCode': 200,
            'body': response
        }
