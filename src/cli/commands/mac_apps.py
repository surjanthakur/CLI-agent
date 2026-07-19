from typing import Annotated

import typer

app = typer.Typer()


@app.command(name="open", help="command helps to open mac apps")
def open(name: Annotated[str, typer.Argument()]):
    pass
