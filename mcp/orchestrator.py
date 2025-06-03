from memory.memory_store import MemoryStore
import json

from agents.classifier_agent import ClassifierAgent
from agents.email_agent import EmailParserAgent
from agents.json_agent import JSONAgent

class Orchestrator:
    def __init__(self):
        self.classifier = ClassifierAgent()
        self.email_agent = EmailParserAgent()
        self.json_agent = JSONAgent()
        self.memory_store = MemoryStore()

    def process(self, input_data: str) -> dict:
        if not isinstance(input_data, str):
            raise ValueError("Input data must be a string")

        format_type, intent = self.classifier.classify(input_data)
        print(f"\n Detected Format: {format_type}")
        print(f" Detected Intent: {intent}")

        output = {
            "format": format_type,
            "intent": intent,
            "parsed": {},
        }

        try:
            if format_type == "Email":
                parsed = self.email_agent.parse_email(input_data)
                output["parsed"] = parsed
            elif format_type == "JSON":
                try:
                    parsed_input = json.loads(input_data)
                    parsed = self.json_agent.process_json(parsed_input)
                    output["parsed"] = parsed
                except json.JSONDecodeError:
                    output["parsed"] = {"error": "Invalid JSON format"}
            elif format_type == "PDF":
                output["parsed"] = {"info": "PDF parsing not implemented yet."}
                # Optionally, raise NotImplementedError or log a message
        except Exception as e:
            # Handle any unexpected errors
            output["parsed"] = {"error": str(e)}

        # Save to memory
        self.memory_store.save_record(
            source="CLI-Test",
            format_type=format_type,
            intent=intent,
            data=json.dumps(output["parsed"])
        )

        return output