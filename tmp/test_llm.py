import sys
from llm_engine import analyze_intent, validate_intent_response, fetch_ranked_context

query = "how many book are available in the libary"
raw = analyze_intent(query)
print("RAW INTENT:", raw)

val = validate_intent_response(raw)
print("VALIDATED INTENT:", val)

keywords = val.get("keywords", [])
print("KEYWORDS:", keywords)

context = fetch_ranked_context(keywords)
print("CONTEXT:", context)
