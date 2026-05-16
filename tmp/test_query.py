import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Set up logging to stdout
import logging
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

from llm_engine import analyze_intent, validate_intent_response, fetch_ranked_context

query = "s6 cse a monday"
raw_intent = analyze_intent(query)
print("Raw Intent:", raw_intent)

validated = validate_intent_response(raw_intent)
print("Validated:", validated)

keywords = validated["keywords"]
intent = validated["intent"]

context = fetch_ranked_context(keywords, intent=intent)
print("Context Items Found:", len(context))
for item in context:
    print(f"- {item['category']}: {item['title']} (Score: {item['score']})")
    print(f"  Details: {item['details']}")
