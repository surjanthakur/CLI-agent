import typer

app = typer.Typer()


@app.command("chat")
def chat_command():
    query = typer.prompt(text="you")
    print(query)
