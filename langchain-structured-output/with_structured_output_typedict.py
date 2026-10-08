from typing import TypedDict, Annotated, Optional, Literal
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")


# schema
class Review(TypedDict):
    key_themes: Annotated[
        list[str], "Write down all the key themes in review in a list"
    ]
    summary: Annotated[str, "A bref summary of the review"]
    sentiment: Annotated[
        Literal["pos", "neg"], "positive, negative or neutral sentiment of review"
    ]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    pros: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write name of the reviewer"]


structured_model = model.with_structured_output(Review)


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
# print(result["summary"])
# print(result["sentiment"])
