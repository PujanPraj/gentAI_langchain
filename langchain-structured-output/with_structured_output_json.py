from pydantic import BaseModel, Field
from typing import Annotated, Optional, Literal
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")


# schema
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Write down all the key themes discussed in the review in a list",
        },
        "summary": {"type": "string", "description": "A brief summary of the review"},
        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "Return sentiment of the review either negative, positive or neutral",
        },
        "pros": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "Write down all the pros inside a list",
        },
        "cons": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "Write down all the cons inside a list",
        },
        "name": {
            "type": ["string", "null"],
            "description": "Write the name of the reviewer",
        },
    },
    "required": ["key_themes", "summary", "sentiment"],
}


structured_model = model.with_structured_output(json_schema)


result = structured_model.invoke("""
    I recently purchased this product and have been using it for a few weeks. Overall, I am very satisfied with its performance and build quality. The product feels sturdy, looks modern, and is easy to use. Setting it up was simple, and it has performed reliably during regular use. I especially like that the features are straightforward and don't require much time to understand.

    There are a few minor drawbacks, such as the price being slightly higher than some similar products and the lack of a few additional features. However, these issues don't significantly affect the overall experience. Considering its quality, reliability, and ease of use, I think it offers good value for money and would recommend it to anyone looking for a dependable product.

    Pros:

    * Good build quality
    * Easy to use
    * Reliable performance
    * Modern design
    * Good for everyday use

    Cons:

    * Slightly expensive
    * Could have more features
    * Limited customization options
""")
print(result)
# print(result.model_dump())
# print(result["summary"])
# print(result["sentiment"])
