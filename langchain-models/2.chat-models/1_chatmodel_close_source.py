from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

result = model.invoke("write a 5 line")

print(result.content)
