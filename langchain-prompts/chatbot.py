from langchain_groq import ChatGroq
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()


model = ChatGroq(model="openai/gpt-oss-120b")


chat_history = [SystemMessage(content="You are a helpful AI assistant")]

while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input in ["exit", "quit", "bye"]:
        print("Bye!")
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f"AI: {result.content}")

print("chat history : ", chat_history)
