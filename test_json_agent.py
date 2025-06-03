# tests/test_json_agent.py

from agents.json_agent import JSONAgent

sample_json = {
    "name": "Ankit Reddy",
    "email": "ankit@example.com",
    "message": "I want a quote for 50 Raspberry Pi units.",
    # phone, company, request_type are missing
}

agent = JSONAgent()
result = agent.process_json(sample_json)

print("\n✅ Reformatted Output:\n", result)