from langchain.messages import AIMessage, SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


model = ChatGroq(model="openai/gpt-oss-120b")

messages = [
    SystemMessage(content="You are a professional AI Engineer"),
    HumanMessage(content="What is message in langchain"),
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)
