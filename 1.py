from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize the model with the specified model name
model = ChatGroq(model="llama3-8b-8192")

# Prompt the user for input
user_input = input("Enter your message: ")

# Example interaction with the model using user input
result = model.predict(user_input)
print(result)
