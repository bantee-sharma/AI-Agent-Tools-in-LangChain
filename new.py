from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

langs = ["English","Hindi"]

st.header("Multilingual Language Translator")
st.title("Accurate and Efficient Translation Service")

languages = ["English","Hindi","Gujrati","German","Japanese","Spanish"]
col1,col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("source_lang",languages,index=0)
with col2:
    target_lang = st.selectbox("target_lang",languages,index=1)

prompt = PromptTemplate(
    template='''You are language Translator.
    Translate text:{text} from the following language source:{source_lang} into this targated language 
    trget{traget_lang} and return translated text.''',
    input_variables=["text","source_lang","target_lang"])

user_input = st.text_input("type...")
if st.button("Translate"):
    chain = prompt|llm
    