from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful AI bot. Your name is {name}"),
        ("human", "{user_input}"),
    ]
)

prompt = chat_template.invoke({"name": "ponky", "user_input": "What is football"})

print(prompt)
