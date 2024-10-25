import google.generativeai as genai
import os

os.environ["KEY"] = "AIzaSyA8arRfdpDVfkDwKPNO4QSnrpEOpOlk__4"
genai.configure(api_key=os.environ["KEY"])

model = genai.GenerativeModel("models/gemini-pro")

def generate_contet(prompt):
    response = model.generate_content(prompt)
    return response.text
