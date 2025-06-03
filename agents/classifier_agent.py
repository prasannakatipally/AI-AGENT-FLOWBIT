# agents/classifier_agent.py

import os
from typing import Tuple
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Updated model configuration
generation_config = {
    "temperature": 0.2,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 100,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

class ClassifierAgent:
    def __init__(self):
        # Initialize model in __init__ to handle potential errors
        try:
            self.model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",  # Updated model name
                generation_config=generation_config,
                safety_settings=safety_settings
            )
        except Exception as e:
            print(f"Error initializing model: {e}")
            self.model = None

    def detect_format(self, content: str) -> str:
        # Naive rule-based detection
        if content.strip().startswith("{"):
            return "JSON"
        elif "From:" in content or "Subject:" in content:
            return "Email"
        else:
            return "PDF"

    def detect_intent(self, content: str) -> str:
        if not self.model:
            return "Other"  # Fallback if model failed to initialize
            
        prompt = f"""You're an AI that classifies business document intent. 
Content: {content}
Identify the intent from [Invoice, RFQ, Complaint, Regulation, Query, Other].
Respond with one word only.
"""

        try:
            response = self.model.generate_content(prompt)
            
            if response.candidates and response.candidates[0].content.parts:
                intent = response.candidates[0].content.parts[0].text.strip()
                return intent
            return "Other"
        except Exception as e:
            print(f"Error detecting intent: {e}")
            return "Other"

    def classify(self, content: str) -> Tuple[str, str]:
        format_type = self.detect_format(content)
        intent_type = self.detect_intent(content)
        return format_type, intent_type