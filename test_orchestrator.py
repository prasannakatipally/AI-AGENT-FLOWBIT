# tests/test_orchestrator.py

from mcp.orchestrator import Orchestrator

sample_email = """
From: Riya Mehta <riya@bizco.com>
Subject: Urgent RFQ for AI Modules

Hi,

Could you send us a quote for 20 AI Vision modules?

Thanks,
Riya
"""

sample_json = """
{
  "name": "Manoj Kumar",
  "email": "manoj@sample.org",
  "message": "Requesting a price breakdown for sensors."
}
"""

orchestrator = Orchestrator()

print("\n=== Testing Email Input ===")
print(orchestrator.process(sample_email))

print("\n=== Testing JSON Input ===")
print(orchestrator.process(sample_json))