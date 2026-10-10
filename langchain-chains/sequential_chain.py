from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

prompt1 = PromptTemplate(
    template="Give me detail explanation on {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Give me 3 point summary from the following text \n {text}",
    input_variables=["text"],
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "Football"})
print(result)


chain.get_graph().print_ascii()
