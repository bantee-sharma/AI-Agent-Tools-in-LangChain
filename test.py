from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

'print(llm.invoke("top news in india"))'

search = DuckDuckGoSearchRun()

print(search.invoke('top news in india'))