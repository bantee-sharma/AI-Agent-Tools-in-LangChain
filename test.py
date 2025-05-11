from langchain_core.tools import tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain import hub
from pydantic import BaseModel
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")



@tool
def weather(city:str)->int:
    "Find the weather of a given city"
    return f"The weather in this{city} is 25°C."


search = DuckDuckGoSearchRun()

prompt = hub.pull('hwchase17/react')


agent = create_react_agent(
    llm=llm,
    tools = [search,weather],
    prompt=prompt,
)

agent_ex = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=[search,weather],
    
)

query = 'Multiply these numbers 3 and 5. and add 3 and 5'
res = agent_ex.invoke({"input":query})

print(res['output'])
