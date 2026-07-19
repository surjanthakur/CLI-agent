from ..tools.macos import mac_finder

import typer

app = typer.Typer()


@app.command("open", help="command helps to open mac apps")
def open_command(name: list[str] = typer.Argument(...)):
    extract_name = " ".join(name)
    mac_finder.open_app(app_name=extract_name)


@app.command("close")
def close_command(name: list[str] = typer.Argument(...)):
    extract_name = " ".join(name)
    mac_finder.close_app(app_name=extract_name)


@app.command("hide")
def hide_command(name: list[str] = typer.Argument(...)):
    extract_name = " ".join(name)
    mac_finder.hide_app(app_name=extract_name)


@app.command("unhide")
def unhide_command(name: list[str] = typer.Argument(...)):
    extract_name = " ".join(name)
    mac_finder.unhide_app(app_name=extract_name)
