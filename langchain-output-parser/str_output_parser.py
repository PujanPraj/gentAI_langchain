from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# this can't give structured output
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm)

# 1st prompt -> detail report
template1 = PromptTemplate(
    template="Write a detail report on {topic}", input_variables=["topic"]
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. \n {text}",
    input_variables=["text"],
)

prompt1 = template1.invoke({"topic": "Black hole"})
result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content})
result2 = model.invoke(prompt2)

print(result2.content)
