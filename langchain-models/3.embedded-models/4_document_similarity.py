from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
document = [
    "Kathmandu is the capital city of Nepal. It is known for its rich culture and historic temples.",
    "Delhi is the capital city of India. It is a major political and cultural center of the country.",
    "Kolkata is the capital city of West Bengal. It is known for its literature, art, and colonial history.",
    "Paris is the capital city of France. It is famous for its art, architecture, fashion, and the Eiffel Tower.",
]

query = "Tell me about Paris"
doc_embedding = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embedding)[0]
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print("================================")
print(query)

print("================================")
print(document[index])

print("================================")
print("similarity score is : ", score)
