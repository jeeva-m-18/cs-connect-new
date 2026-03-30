import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    print("API Key not found in environment!")
else:
    masked_key = api_key[:10] + "..." + api_key[-4:]
    print(f"Testing API Key: {masked_key}")
    try:
        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": "test"}],
            model="llama-3.3-70b-versatile",
            max_tokens=5
        )
        print("Success! The API key is valid.")
    except Exception as e:
        print(f"Error: {e}")
