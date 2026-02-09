from abc import ABC, abstractmethod

class LLMProvider(ABC):

    @abstractmethod
    def generate_structured_output(
        self,
        system_prompt: str,
        user_prompt: str,
        tools: list,
        output_schema: dict
    ) -> dict:
        pass
