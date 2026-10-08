from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


# this both will work, there is no validation in typeddict
new_person: Person = {"name": "kenji", "age": 30}
new_person: Person = {"name": "kenji", "age": "adkslfj"}

print(new_person)
