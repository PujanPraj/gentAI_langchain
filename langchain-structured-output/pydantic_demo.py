from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Person(BaseModel):
    name: str = "ram"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)


new_person = {"email": "abc@gmail.com", "cgpa": 8}

person = Person(**new_person)
print(person.model_dump())
print(person.model_dump_json())
# print(type(person))
