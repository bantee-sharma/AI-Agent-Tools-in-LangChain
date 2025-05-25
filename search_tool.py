from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun,tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub

# step-1
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
search_tool = DuckDuckGoSearchRun()

# step-2
prompt = hub.pull("hwchase17/react")

# step-3
agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

# step-4
agent_executer = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose= True,
    handle_parsing_errors=True
)

response = agent_executer.invoke({"input":'3 ways to reach delhi from jewar'})
print(response)