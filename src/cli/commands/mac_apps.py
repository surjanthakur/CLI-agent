from typing import Annotated
from ...tools.macos import mac_finder

import typer

app = typer.Typer()


@app.command(help="command helps to open mac apps")
def open_command(name: Annotated[str, typer.Argument()]):
    mac_finder.open_app(app_name=name)


@app.command()
def close_command(name: Annotated[str, typer.Argument()]):
    mac_finder.close_app(app_name=name)


@app.command()
def hide_command(name: Annotated[str, typer.Argument()]):
    mac_finder.hide_app(app_name=name)


@app.command()
def unhide_command(name: Annotated[str, typer.Argument()]):
    mac_finder.unhide_app(app_name=name)
