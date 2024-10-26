import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-pro")

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text
