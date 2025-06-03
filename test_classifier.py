# test_classifier.py

from agents.classifier_agent import ClassifierAgent

agent = ClassifierAgent()

sample_email = """
From: customer@example.com
Subject: Request for Quotation

Hello, please send us a quotation for 100 units of item XYZ.
"""

format_type, intent = agent.classify(sample_email)

print("Format:", format_type)
print("Intent:", intent)
