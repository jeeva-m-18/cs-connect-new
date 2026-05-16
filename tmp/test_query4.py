import sys
import os
from dotenv import load_dotenv

load_dotenv()
from llm_engine import analyze_intent, validate_intent_response, fetch_ranked_context, generate_chatbot_response

queries = [
    "give me syllabus for s6",
    "how are theory and lab exams evaluated?"
]

for query in queries:
    print(f"\n--- QUERY: {query} ---")
    response = generate_chatbot_response(query, [])
    print(f"Response Dict: {response}")
