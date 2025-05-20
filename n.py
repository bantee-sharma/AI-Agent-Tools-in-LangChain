from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent,AgentExecutor
from langchain_community.tools import tool

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

search = DuckDuckGoSearchRun()

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=[search],
    prompt=prompt
)

agent_exe = AgentExecutor(
    agent=agent,
    tools=[search],
    verbose=True
)

query = "Weather of jewar"
res = agent_exe.invoke({"input":query})
print(res)