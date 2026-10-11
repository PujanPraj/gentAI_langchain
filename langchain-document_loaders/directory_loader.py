from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

loader = DirectoryLoader(path="books", glob="*.pdf", loader_cls=PyPDFLoader)
docs = loader.lazy_load()
# print(len(docs))
# print(docs[281].page_content)
# print(docs[281].metadata)

for document in docs:
    print(document.metadata)
