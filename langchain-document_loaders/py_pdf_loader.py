from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

loader = PyPDFLoader(file_path="Unit-3-Cloud-Virtualization-Technology.pdf")
docs = loader.load()

# print(len(docs))
print(docs[0].page_content)
print(docs[1].metadata)
