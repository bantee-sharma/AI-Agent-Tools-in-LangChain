from langchain_google_genai import  ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = [SystemMessage(content="You are a helpfull AI Assistant.")]
while True:
    question = input("Ask Question: ").strip()
    chat_history.append(HumanMessage(content=question))
    if question.lower() in ["exit","quit"]:
        print("Exiting..., Have a good day!")
        break
    else:
        response = llm.invoke(chat_history)
        chat_history.append(AIMessage(content=response.content))
        print("AI: ",response.content)
print(chat_history)