from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = [SystemMessage(content="You are a helpfull AI")]

print("Statr chatting wiht AI type 'exit' to stop:")

while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.strip().lower() == 'exit':
        print("Byee")
        break
    else:
        res = llm.invoke(chat_history)
        chat_history.append(AIMessage(content=res.content))
        print("AI :",res.content)
print(chat_history)
