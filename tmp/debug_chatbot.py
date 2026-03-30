import os
import logging
from dotenv import load_dotenv
from llm_engine import analyze_intent, validate_intent_response, fetch_ranked_context, build_safe_context

# Setup logging
logging.basicConfig(level=logging.INFO)
load_dotenv()

def debug_chatbot(user_input):
    print(f"\n--- Debugging: '{user_input}' ---")
    
    # 1. Analyze Intent
    raw_intent = analyze_intent(user_input)
    print(f"Raw Intent from LLM: {raw_intent}")
    
    validated = validate_intent_response(raw_intent)
    print(f"Validated: {validated}")
    
    intent = validated["intent"]
    keywords = validated["keywords"]
    
    if not keywords:
        print("No keywords extracted.")
        return

    # 2. Fetch Context
    print(f"Fetching context for keywords: {keywords}")
    context_items = fetch_ranked_context(keywords)
    print(f"Number of context items found: {len(context_items)}")
    
    for i, item in enumerate(context_items):
        print(f"Item {i+1}: {item['category']} - {item['title']} (Score: {item['score']})")

    # 3. Build context
    context = build_safe_context(context_items)
    print("\n--- Final Context String ---")
    print(context)
    print("----------------------------")

if __name__ == "__main__":
    debug_chatbot("who i hod??")
