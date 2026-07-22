from ..agent.llm import qwen_llm_response
import typer
from rich import print

app = typer.Typer()


@app.command("chat", help="Start an interactive chat prompt")
def chat_command():
    while True:
        query = typer.prompt(text=">")
        if query == "quit":
            break
        print(f"you: [blue]{query}[/blue]")
        stream = qwen_llm_response()
        for chunk in stream:
            if chunk.content:  # Each chunk has .content
                print(
                    f"Clark-agent: [green]{chunk.content}[/green]", end="", flush=True
                )
        print()
