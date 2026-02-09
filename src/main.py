import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import typer

from .providers.openai_provider import OpenAIProvider
from .providers.claude_provider import ClaudeProvider
from .providers.gemini_provider import GeminiProvider
from .agent.runtime import AgentRuntime


app = typer.Typer()

@app.command()
def run(
    model: str = typer.Option(..., help="gpt-5.2 | claude-opus-4.6 | gemini-3"),
    input: str = typer.Option(..., help="User instruction")
):
    providers = {
        "gpt-5.2": OpenAIProvider(),
        "claude-opus-4.6": ClaudeProvider(),
        "gemini-3": GeminiProvider()
    }

    if model not in providers:
        raise typer.BadParameter("Invalid model")

    agent = AgentRuntime(
        provider=providers[model],
        allowed_tools=["createWorkflow"]
    )

    print("\n🟡 PREVIEW MODE")
    preview = agent.preview(input)
    print(preview)

    confirm = typer.prompt("\nApply workflow? (yes/no)")
    if confirm.lower() == "yes":
        print("\n🔴 EXECUTION MODE")
        agent.apply(preview)

if __name__ == "__main__":
    app()
