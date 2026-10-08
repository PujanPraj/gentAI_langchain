from dotenv import load_dotenv

load_dotenv()

# from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# model = ChatGroq(model="openai/gpt-oss-120b", temperature=1.5)

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is capital of nepal")

print(result.content)
