from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

# 1st prompt -> detail report
template1 = PromptTemplate(
    template="Write a detail report on {topic}", input_variables=["topic"]
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template=("Summarize the following text in exactly 5 lines. " "{text}"),
    input_variables=["text"],
)

parser = StrOutputParser()
chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({"topic": "Black hole"})
print(result)
