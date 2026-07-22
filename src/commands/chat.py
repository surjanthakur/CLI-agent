from ..agent.llm import qwen_llm_response

import typer
from rich import print
from rich.console import Console
from rich.live import Live

app = typer.Typer()

console = Console()


@app.command("chat", help="Start an interactive chat with agent")
def chat_command():
    console.print(
        "[bold cyan]Chat with Clark-Agent (type 'quit' to exit)[/bold cyan]\n"
    )
    while True:
        try:
            query = typer.prompt("You", prompt_suffix="> ")

            if query.lower() in ["quit", "exit", "q"]:
                console.print("[yellow]Goodbye see you soon bro![/yellow]")
                break

            stream = qwen_llm_response(query)

            console.print("[bold green]AI:[/bold green] ", end="")

            with Live(
                console=console,
                refresh_per_second=60,
                vertical_overflow="visible",
            ) as live:
                live.update("[bold green]AI:[/bold green] ")
                full_response = ""

                for chunk in stream:
                    if chunk.content:
                        full_response += chunk.content
                        live.update(
                            f"[bold green]AI:[/bold green] [blue]{full_response}[/blue]"
                        )

            console.print()  # New line after response
            console.print("─" * 80)  # Separator

        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted. Type 'quit' to exit.[/yellow]")
            continue
        except Exception as err:
            console.print(f"[red]Error: {err}[/red]")
            continue
