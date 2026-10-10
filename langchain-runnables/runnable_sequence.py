from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

promt2 = PromptTemplate(
    template="Explain the following joke \n {text}", input_variables=["text"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, promt2, model, parser)
result = chain.invoke({"topic": "AI"})
print(result)
