import logging

import typer
from rich import print

from ..tools.macos import apps

app = typer.Typer()

logger = logging.getLogger(__name__)


# opne app
@app.command("open", help="Open an application by name")
def open_command(name: list[str] = typer.Argument(..., help="Name of the app to open")):
    try:
        extract_name = " ".join(name)
        apps.open_app(extract_name)

    except KeyboardInterrupt:
        logger.info("Operation cancelled by user while opening app")
        print("[red]Operation cancelled by user.[/red]")
    else:
        print(f"[green] opened app {extract_name}...[/green]\n")


# close app
@app.command("close", help="Close an application by name")
def close_command(
    name: list[str] = typer.Argument(..., help="Name of the app to close"),
):
    try:
        extract_name = " ".join(name)
        apps.close_app(extract_name)

    except KeyboardInterrupt:
        logger.info("Operation cancelled by user while closing app")
        print("[red]Operation cancelled by user.[/red]")
    else:
        print(f"[green] closed app {extract_name}...[/green]\n")


# hide app
@app.command("hide", help="Hide an application by name")
def hide_command(name: list[str] = typer.Argument(..., help="Name of the app to hide")):
    try:
        extract_name = " ".join(name)
        apps.hide_app(extract_name)

    except KeyboardInterrupt:
        logger.info("Operation cancelled by user while hiding app")
        print("[red]Operation cancelled by user.[/red]")
    else:
        print(f"[green] hid app {extract_name}...[/green]\n")


# unhide app
@app.command("unhide", help="Unhide an application by name")
def unhide_command(
    name: list[str] = typer.Argument(..., help="Name of the app to unhide"),
):
    try:
        extract_name = " ".join(name)
        apps.unhide_app(extract_name)

    except KeyboardInterrupt:
        logger.info("Operation cancelled by user while unhiding app")
        print("[red]Operation cancelled by user.[/red]")
    else:
        print(f"[green] unhid app {extract_name}...[/green]\n")
