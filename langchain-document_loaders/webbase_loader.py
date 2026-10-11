from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    WebBaseLoader,
)
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

url = "https://www.daraz.com.np/products/soundcore-r50i-true-wireless-in-ear-earbuds-tws-with-30h-playtime-clear-calls-high-bass-ipx5-water-resistant-soundcore-connect-app-with-22-preset-eqs-quick-connectivity-i128040852-s1035237651.html?scm=1007.51610.379274.0&pvid=bade527d-c3e6-465c-b0a2-12b143aca1af&search=flashsale&spm=a2a0e.tm80335409.FlashSale.d_128040852"
loader = WebBaseLoader(url)

prompt = PromptTemplate(
    template="Write the 3 point summary on the {text} and answer the question of {question}",
    input_variables=["text", "question"],
)

parser = StrOutputParser()

docs = loader.load()
# print(len(docs))
# print(docs[0].page_content)
chain = prompt | model | parser

result = chain.invoke(
    {
        "text": docs[0].page_content,
        "question": "What is the topic of product and what is the price",
    }
)
print(result)
