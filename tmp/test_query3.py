import sys
import os
from dotenv import load_dotenv

load_dotenv()
from llm_engine import analyze_intent, validate_intent_response, fetch_db_context, fetch_ranked_context, generate_chatbot_response

queries = [
    "who is teaching computer graphics for s6"
]

for query in queries:
    print(f"\n--- QUERY: {query} ---")
    raw_intent = analyze_intent(query)
    validated = validate_intent_response(raw_intent)
    keywords = validated["keywords"]
    intent = validated["intent"]

    print(f"Keywords: {keywords}")
    print(f"Intent: {intent}")

    context_items = fetch_ranked_context(keywords, intent=intent)
    print(f"Num items: {len(context_items)}")
    for item in context_items:
        print(item)
    
    response = generate_chatbot_response(query, [])
    print(f"\nLLM Response: {response['message']}")
