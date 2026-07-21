from ..tools.macos import apps
from ..utils.exceptions import handle_exceptions

from rich import print

import typer

app = typer.Typer()


# opne app
@app.command("open", help="Open an application by name")
def open_command(name: list[str] = typer.Argument(..., help="Name of the app to open")):
    extract_name = " ".join(name)
    print(f"[green] opened {extract_name} [/green]")
    handle_exceptions(apps.open_app, extract_name)


# close app
@app.command("close", help="Close an application by name")
def close_command(
    name: list[str] = typer.Argument(..., help="Name of the app to close")
):
    extract_name = " ".join(name)
    print(f"[green] closed {extract_name} [/green]")
    handle_exceptions(apps.close_app, extract_name)


# hide app
@app.command("hide", help="Hide an application by name")
def hide_command(name: list[str] = typer.Argument(..., help="Name of the app to hide")):
    extract_name = " ".join(name)
    print(f"[green] hid {extract_name} [/green]")
    handle_exceptions(apps.hide_app, extract_name)


# unhide app
@app.command("unhide", help="Unhide an application by name")
def unhide_command(
    name: list[str] = typer.Argument(..., help="Name of the app to unhide")
):
    extract_name = " ".join(name)
    print(f"[green] unhid {extract_name} [/green]")
    handle_exceptions(apps.unhide_app, extract_name)
