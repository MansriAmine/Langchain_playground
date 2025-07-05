from langchain_groq import ChatGroq
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize the model with the specified model name
model = ChatGroq(model="llama-3.3-70b-versatile")


class AnswerOutputParser(BaseOutputParser):
    def parse(self, text: str):
        """Parse the output of an LLM call"""
        return text.strip().split('answer =')




# Prompt the user for input
template = """You are a helpful assistant that solves math problems and shows your work.
        output each step then retunr the answer in the following format : answer = <answer here>.
        make sure to output answer in all lowercases and to have exactly one space and one equal sign following it.
        """

human_template = "{problem}"

chat_promt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

user_input = chat_promt.format_messages(problem="2x^2 - 5x + 3 = 0")

# Example interaction with the model using user input
result = model.predict_messages(user_input)
parsed = AnswerOutputParser().parse(result.content)
steps, answer = parsed

print(steps, answer)
