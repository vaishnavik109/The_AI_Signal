from .base import LLMProvider


class ClaudeProvider(LLMProvider):

    def generate_structured_output(self, system_prompt, user_prompt, tools, output_schema):
        return {
            "workflow": {
                "name": "Overdue Task Handler",
                "trigger": "task.overdue",
                "steps": [
                    {
                        "type": "update",
                        "entity": "Task",
                        "update": {"status": "urgent"}
                    }
                ]
            }
        }
