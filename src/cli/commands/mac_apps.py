from typing import Annotated
from tools.macos import mac_finder

import typer

mac_app = typer.Typer()


@mac_app.command(name="open", help="command helps to open mac apps")
def open(name: Annotated[str, typer.Argument()]):
    mac_finder.open_app(app_name=name)


@mac_app.command(name="close")
def close(name: Annotated[str, typer.Argument()]):
    mac_finder.close_app(app_name=name)


@mac_app.command(name="hide")
def close(name: Annotated[str, typer.Argument()]):
    mac_finder.hide_app(app_name=name)


@mac_app.command(name="unhide")
def close(name: Annotated[str, typer.Argument()]):
    mac_finder.unhide_app(app_name=name)
