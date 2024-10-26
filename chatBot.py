import google.generativeai as genai
import os

# os.environ["KEY"] = "AIzaSyA8arRfdpDVfkDwKPNO4QSnrpEOpOlk__4"
api_key = os.environ.get('API_KEY')

genai.configure(api_key)

model = genai.GenerativeModel("models/gemini-pro")

def generate_contet(prompt):
    response = model.generate_content(prompt)
    return response.text
