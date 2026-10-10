from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")


class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="City of the person")


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

# prompt = template.invoke({"place": "nepali"})
# print(prompt)
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

chain = template | model | parser
result = chain.invoke({"place": "nepal"})
print(result)
