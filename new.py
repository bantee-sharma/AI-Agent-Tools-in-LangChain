from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import tool, AgentExecutor, create_react_agent
from langchain import hub
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.output_parsers import StructuredOutputParser
import requests

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

search = DuckDuckGoSearchRun()
prompt = hub.pull("hwchase17/react")

#parser = StructuredOutputParser()

@tool
def weather(city:str)->str:
    "Fetch the current weather"
    url = "https://api.weatherstack.com/current?access_key=2eab0e8b57aa4c3082a9f22e95baa467"
    city_name = {"query":city}
    response = requests.get(url=url,params=city_name)
    return response.json()

tools = [search,weather]

llm_bind = llm.bind_tools(tools)

print(llm_bind({"query" :"weather of noida"}))

