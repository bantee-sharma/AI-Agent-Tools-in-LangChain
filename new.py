from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import tool, AgentExecutor, create_react_agent
from langchain import hub

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
