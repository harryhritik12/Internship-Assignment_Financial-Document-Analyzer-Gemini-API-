import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure with API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load a free Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Run a simple test
response = model.generate_content("Give me one line of financial advice")
print(response.text)
