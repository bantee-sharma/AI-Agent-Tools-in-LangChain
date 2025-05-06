from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun,tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
import re

load_dotenv()

# step-1
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
search_tool = DuckDuckGoSearchRun()


@tool

def add(input: str) -> int:
    """Add two numbers. Extracts any two integers from the input."""
    numbers = list(map(int, re.findall(r'\d+', input)))
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to add.")
    return numbers[0] + numbers[1]

# step-2
prompt = hub.pull("hwchase17/react")

#step-3
agent = create_react_agent(
    llm=llm,
    tools=[search_tool,add],
    prompt=prompt
)

agent_executer = AgentExecutor(
    agent=agent,
    tools=[search_tool,add],
    verbose=True
)


query = "3 ways to go delhi from jewar"
res = agent_executer.invoke({"input":query})
print(res)








