from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import tool, create_react_agent, AgentExecutor
from dotenv import load_dotenv
import requests
from langchain import hub

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

@tool
def weather(city:str)->str:
    "Fetch the current weather of the city"
    url = 'https://api.weatherstack.com/current?access_key=2eab0e8b57aa4c3082a9f22e95baa467&query={city}'
    response = requests.get(url)
    return response.json()

prompt=hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=[weather],
    prompt = prompt
)

agent_exe = AgentExecutor(
    agent=agent,
    tools=[weather],
    verbose=True
)

query = "waht is the weather in Bhopal"
result = agent_exe.invoke({"input":query})
print(result)



