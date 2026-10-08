from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful customer support agent"),
        MessagesPlaceholder("chat_history"),
        ("human", "{query}"),
    ]
)

chat_history = [
    ("human", "I want to request a refund for my order #12345."),
    (
        "ai",
        "Your refund request for order #12345 has been initiated. It will be processed in 3-5 business days.",
    ),
]
# load chat history
# with open("chat_history.txt") as f:
#     chat_history.extend(f.readlines())

print(chat_history)

# create prompt
result = chat_template.invoke(
    {"chat_history": chat_history, "query": "where is my refund"}
)
print(result)
