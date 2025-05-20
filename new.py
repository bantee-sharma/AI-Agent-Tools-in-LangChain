from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent,AgentExecutor
from duckduckgo_search import DuckDuckGoSearchException

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

search = DuckDuckGoSearchRun()

prompt = hub.pull("hwchase17/react")

agent  = create_react_agent(
    llm=llm,
    prompt=prompt,
    tools=[search]
)

agent_executer = AgentExecutor(
    agent=agent,
    tools=[search],
    verbose=True,
    handle_parsing_errors=True
)

'''response = agent_executer.invoke({"input":'3 ways to reach delhi from jewar'})
print(response)'''

try:
    result = search.run("how to get from jewar to delhi")
except DuckDuckGoSearchException as e:
    print("Encountered a rate limit error. Waiting for a while before retrying...")
     # Adjust sleep time as needed.
    result = search.run("how to get from jewar to delhi")