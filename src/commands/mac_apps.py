from ..tools.macos import apps

import typer

app = typer.Typer()


@app.command("open", help="Open an application by name")
def open_command(name: list[str] = typer.Argument(..., help="Name of the app to open")):
    extract_name = " ".join(name)
    apps.open_app(app_name=extract_name)


@app.command("close", help="Close an application by name")
def close_command(
    name: list[str] = typer.Argument(..., help="Name of the app to close")
):
    extract_name = " ".join(name)
    apps.close_app(app_name=extract_name)


@app.command("hide", help="Hide an application by name")
def hide_command(name: list[str] = typer.Argument(..., help="Name of the app to hide")):
    extract_name = " ".join(name)
    apps.hide_app(app_name=extract_name)


@app.command("unhide", help="Unhide an application by name")
def unhide_command(
    name: list[str] = typer.Argument(..., help="Name of the app to unhide")
):
    extract_name = " ".join(name)
    apps.unhide_app(app_name=extract_name)
