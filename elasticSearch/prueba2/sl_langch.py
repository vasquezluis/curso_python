import streamlit as st
import tempfile
import os
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

def main():
    
    load_dotenv()

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV")

    user_csv = st.file_uploader("Upload your CSV file", type="csv")

    if user_csv is not None:
        # save the uploaded file to a temporary location
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(user_csv.getvalue())
        temp_file.close()

        user_question = st.text_input("Ask your question about your CSV")

        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm, [temp_file.name], verbose=True)

        if user_question is not None and user_question != "":
            response = agent.run(user_question)
            st.write(f"Your question was: {user_question}")
            st.write(f"The answer is: {response}")

        os.unlink(temp_file.name)

if __name__ == "__main__":
    main()
