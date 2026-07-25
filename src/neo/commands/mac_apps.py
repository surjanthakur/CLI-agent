import typer
from rich import print

from ..core.logging import my_logger
from ..tools.macos import apps

app = typer.Typer()


# opne app
@app.command("open", help="Open an application by name")
def open_command(
    name: list[str] = typer.Argument(..., help="Name of the app to open")  # noqa: B008
):
    try:
        extract_name = " ".join(name)
        apps.open_app(extract_name)

    except KeyboardInterrupt:
        my_logger.info("Operation cancelled by user while opening app")
        print("[red]Operation cancelled by user.[/red]")
        raise typer.Exit(1)


# close app
@app.command("close", help="Close an application by name")
def close_command(
    name: list[str] = typer.Argument(..., help="Name of the app to close")  # noqa: B008
):
    try:
        extract_name = " ".join(name)
        apps.close_app(extract_name)

    except KeyboardInterrupt:
        my_logger.info("Operation cancelled by user while closing app")
        print("[red]Operation cancelled by user.[/red]")


# hide app
@app.command("hide", help="Hide an application by name")
def hide_command(
    name: list[str] = typer.Argument(..., help="Name of the app to hide")  # noqa: B008
):
    try:
        extract_name = " ".join(name)
        apps.hide_app(extract_name)

    except KeyboardInterrupt:
        my_logger.info("Operation cancelled by user while hiding app")
        print("[red]Operation cancelled by user.[/red]")


# unhide app
@app.command("unhide", help="Unhide an application by name")
def unhide_command(
    name: list[str] = typer.Argument(..., help="app name to unhide")  # noqa: B008
):
    try:
        extract_name = " ".join(name)
        apps.unhide_app(extract_name)

    except KeyboardInterrupt:
        my_logger.info("Operation cancelled by user while unhiding app")
        print("[red]Operation cancelled by user.[/red]")
