# agents/email_agent.py

import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class EmailParserAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def parse_email(self, email_text: str) -> dict:
        prompt = f"""
You're an intelligent email parser.
Analyze the email below and extract the following:
1. Sender Name
2. Request Intent (Invoice, RFQ, Complaint, Query, Regulation, Other)
3. Urgency (High, Medium, Low)

Respond in JSON format with keys:
sender, intent, urgency

EMAIL:
{email_text}
"""
        try:
            response = self.model.generate_content(prompt)
            response_text = response.text.strip()

            print("🔍 Raw LLM Output:\n", response_text)  # <== DEBUG PRINT

            # Try cleaning markdown if any
            if response_text.startswith("```json"):
                response_text = response_text.replace("```json", "").replace("```", "").strip()

            parsed = json.loads(response_text)
            return parsed
        except Exception as e:
            print("❌ Error parsing email:", e)
            return {"sender": "", "intent": "", "urgency": ""}