from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt = PromptTemplate(
    template='''Answer the following Question{question}
    Answer: Let's think step by step.''',
    input_variables=["question"]
)

chain = prompt | llm

# Streamlit UI
st.title("🤖 LangChain Question Answering Model")
st.write("Ask me anything!")
user_input = st.text_input("Enter your question")
if st.button('Get Answer'):
    res = chain.invoke({"question":user_input})
    st.write(res.content)
