from .schemas import WorkflowOutput
from .permissions import check_tool_permission
from ..tools.workflow_tools import create_workflow


class AgentRuntime:

    def __init__(self, provider, allowed_tools):
        self.provider = provider
        self.allowed_tools = allowed_tools

    def preview(self, user_input):
        result = self.provider.generate_structured_output(
            system_prompt="You are a safe workflow agent",
            user_prompt=user_input,
            tools=self.allowed_tools,
            output_schema=None
        )

        validated = WorkflowOutput(**result)
        return validated

    def apply(self, validated_output):
        check_tool_permission("createWorkflow", self.allowed_tools)
        create_workflow(validated_output.workflow.dict())
