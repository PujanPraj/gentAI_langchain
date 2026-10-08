from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


documents = [
    "Kathmandu is the capital of Nepal",
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France",
]
# text = "Kathmandu is the capital of Nepal"
# vector_text = embedding.embed_query(text)
vector_docs = embedding.embed_documents(documents)
print(str(vector_docs))
