import sys
import os
from dotenv import load_dotenv

load_dotenv()
from llm_engine import generate_chatbot_response

query = "s6 cse a monday"
response = generate_chatbot_response(query, [])
print("LLM Response:")
print(response['message'])
