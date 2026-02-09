from .base import LLMProvider


class OpenAIProvider(LLMProvider):

    def generate_structured_output(self, system_prompt, user_prompt, tools, output_schema):
        # MOCKED RESPONSE (allowed)
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
