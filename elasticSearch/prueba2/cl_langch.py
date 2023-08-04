import tempfile
import os
import pandas as pd
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import tiktoken


def tokinizer(string: str, encoding_name: str) -> int:
    """Return the number of tokens in a text strng"""

    # tokenizer config
    # encoding = tiktoken.get_encoding('cl100k_base')
    # encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def main():
    load_dotenv()
    csv_file = "/home/luii/Documents/curso_python/elasticSearch/prueba2/campaigns_release.csv"

    if os.path.exists(csv_file):
        # save the CSV file to a temporary location
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file_name = temp_file.name
        temp_file.close()

        # Copy the CSV file to the temporary location
        os.system(f"cp {csv_file} {temp_file_name}")

        user_question = input("Ask your question about your CSV: ")

        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm, [temp_file_name], verbose=True)
        print('agent: ', agent)

        if user_question != "":
            # Read CSV with low_memory=False to avoid DtypeWarning
            df = pd.read_csv(temp_file_name, low_memory=False)

            # Specify the data type for column 10 if needed
            # df['Column10'] = df['Column10'].astype(str)

            response = agent.run(user_question)
            print(f"Your question was: {user_question}")
            print(f"The answer is: {response}")
            print(f"number of tokens for question: {tokinizer(user_question, 'gpt-3.5-turbo')}")
            print(f"number of tokens for answer: {tokinizer(response, 'gpt-3.5-turbo')}")

        os.unlink(temp_file_name)


if __name__ == "__main__":
    main()
