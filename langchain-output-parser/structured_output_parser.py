from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")


schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 fact about {topic} \n {format_description}",
    input_variables=["topic"],
    partial_variables={"format_description": parser.get_format_instructions()},
)

# prompt = template.invoke({"topic": "black hole"})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

chain = template | model | parser
result = chain.invoke({"topic": "black hole"})
print(result)
