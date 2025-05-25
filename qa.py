from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

st.title("Question Answering Bot")

user_input = st.text_input("Enter you Text:")

from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are a helpful AI assistant.\n"
        "If someone asks your name, say: 'Hi, I'm Chitti the Robot. Speed 1 terahertz, memory 1 zigabyte.'\n"
        "Answer the following question:\n"
        "{question}\n"
        "Answer:"
    )
)


if st.button("Submit"):
    chain = prompt|llm
    result = chain.invoke(user_input)
    st.write(result.content)