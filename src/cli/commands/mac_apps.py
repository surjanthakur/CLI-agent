from typing import Annotated
from tools.macos import mac_finder

import typer

app = typer.Typer()


@app.command(name="open", help="command helps to open mac apps")
def open(name: Annotated[str, typer.Argument()]):
    mac_finder.open_app(app_name=name)


@app.command(name="close")
def close(name: Annotated[str, typer.Argument()]):
    mac_finder.close_app(app_name=name)


@app.command(name="hide")
def close(name: Annotated[str, typer.Argument()]):
    mac_finder.hide_app(app_name=name)


@app.command(name="unhide")
def close(name: Annotated[str, typer.Argument()]):
    mac_finder.unhide_app(app_name=name)
