from langchain_groq import ChatGroq
from langchain.prompts.chat import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize the model with the specified model name
model = ChatGroq(model="llama-3.3-70b-versatile")

# Prompt the user for input
template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_promt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

user_input = chat_promt.format_messages(input_language="English",
                                      output_language="French",
                                      text=" Gojo is the GOAT.")

# Example interaction with the model using user input
result = model.predict_messages(user_input)
print(result.content)
