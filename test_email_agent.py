# tests/test_email_agent.py

from agents.email_agent import EmailParserAgent

sample_email = """
From: Ramya Ananth <ramya@clientco.com>
Subject: Urgent RFQ for Q3 Deliverables

Hi team,

We urgently need a quotation for 200 units of the XJ-202 motherboard, delivery by August. Please treat this request as high priority.

Thanks,
Ramya
"""

agent = EmailParserAgent()
parsed_output = agent.parse_email(sample_email)

print(parsed_output)