from langchain_groq import ChatGroq
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize the model with the specified model name
model = ChatGroq(model="llama-3.3-70b-versatile")


class commaSeparatedListOutputParser(BaseOutputParser):
    def parse(self,text: str):
        return text.strip().split(", ")



# Prompt the user for input
template = """You are a helpful assistant that solves math problems and shows your work.
        a user will pass in a categort, and you should generate 5 objects in that category in a comma separated list.
        Only return a comma separated list , and nothing more."""

human_template = "{text}"

chat_promt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])


# Example interaction with the model using user input
chain = chat_promt | model | commaSeparatedListOutputParser()
result = chain.invoke({"text": "colors"})

print(result)
