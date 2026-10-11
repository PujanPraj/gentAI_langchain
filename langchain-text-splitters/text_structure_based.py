from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Famous Football Players

Lionel Messi is an Argentine footballer known for his dribbling, passing, creativity, and goal-scoring ability.

Cristiano Ronaldo is a Portuguese footballer known for his athleticism, finishing, heading ability, and long career at the highest level.

Pelé was a Brazilian football legend who helped popularize the sport internationally.

Diego Maradona was an Argentine footballer remembered for his exceptional dribbling and influential performances.

Marta is a Brazilian footballer widely recognized for her achievements and influence in women's football.
"""


splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)

chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)
