from typing import Annotated
from tools.macos import mac_finder

import typer

app = typer.Typer()


@app.command(name="open", help="command helps to open mac apps")
def open(name: Annotated[str, typer.Argument()]):
    mac_finder.open_app(app_name=name)
