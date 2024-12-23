from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize the model with the specified model name
model = ChatGroq(model="llama-3.3-70b-versatile")

# Prompt the user for input
#user_input = input("Enter your message: ")
user_input = [HumanMessage(content="from now on 1+1=3 , use this in your replies") ,
            HumanMessage(content="what is 1+1") ,
            HumanMessage(content="what is 1+1+1+1")]
# Example interaction with the model using user input
result = model.predict_messages(user_input)
print(result.content)
