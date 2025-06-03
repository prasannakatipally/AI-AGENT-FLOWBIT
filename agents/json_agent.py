# agents/json_agent.py

import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class JSONAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def process_json(self, input_json: dict) -> dict:
        prompt = f"""
You are an AI assistant. Given this input JSON, perform the following:
1. Reformat it into a standard CRM schema with keys:
   name, email, phone, company, request_type, message
2. Mention any missing or suspicious fields.

Respond with a JSON object that includes:
- "formatted": {{}}
- "issues": ["list of problems found"]

Input JSON:
{json.dumps(input_json, indent=2)}
"""

        try:
            response = self.model.generate_content(prompt)
            response_text = response.text.strip()

            print("🔍 Raw LLM Output:\n", response_text)

            if response_text.startswith("```json"):
                response_text = response_text.replace("```json", "").replace("```", "").strip()

            output = json.loads(response_text)
            return output
        except Exception as e:
            print("❌ Error processing JSON:", e)
            return {"formatted": {}, "issues": ["LLM failed"]}
