import typer

app = typer.Typer()


@app.command("chat", help="Start an interactive chat prompt")
def chat_command():
    query = typer.prompt(text="you")
    print(query)
