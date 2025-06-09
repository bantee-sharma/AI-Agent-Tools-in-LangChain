from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import tool,AgentExecutor,create_react_agent
import requests
from langchain import hub
from typing import TypedDict

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Weather(TypedDict):
    city:str
    location:str
    temperature:str

llm_with = llm.with_structured_output(Weather)


def weather(city:str)->str:
    "fetch the current weather of city."
    url = url = "https://api.weatherstack.com/current?access_key=2eab0e8b57aa4c3082a9f22e95baa467"

    querystring = {"query":city}
    respose = requests.get(url,params=querystring)
    return respose.json()


query = input()
res = llm_with.invoke(query)
print(res)