from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import tool,AgentExecutor,create_react_agent
import requests
from langchain import hub

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

@tool
def weather(city:str)->str:
    "fetch the current weather of city."
    url = url = "https://api.weatherstack.com/current?access_key=2eab0e8b57aa4c3082a9f22e95baa467"

    querystring = {"query":city}
    respose = requests.get(url,params=querystring)
    return respose.json()

prompt = hub.pull("hwchase17/react")
# hwchase17/react

agent = create_react_agent(
    llm=llm,
    tools=[weather],
    prompt=prompt
)

agente_exe = AgentExecutor(
    agent=agent,
    tools=[weather],
    verbose=True
)

query = "Where is delhi?"
result = agente_exe.invoke({"input":query})
print(result)