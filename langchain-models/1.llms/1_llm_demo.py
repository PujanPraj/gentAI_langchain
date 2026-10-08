from dotenv import load_dotenv

load_dotenv()

# ! We don't use this any more
from langchain_openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-instruct")
result = llm.invoke("What is capital of Nepal")
print(result)
