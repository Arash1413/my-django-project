import os
import google.generativeai as genai
from django.conf import settings

def generate_story_continuation(prompt: str) -> str:

    try:
        genai.configure(api_key="AIzaSyDbxQWo07nnQV_58KW7CFIaSgAJHNSL2w4")
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        full_prompt = f"continue this story: '{prompt}'"

        response = model.generate_content(full_prompt)

        # print(response.text)
        return response.text
    except Exception as e:
        print(f"Error generating story: {e}")
        return "Sorry, I couldn't come up with a story right now."

