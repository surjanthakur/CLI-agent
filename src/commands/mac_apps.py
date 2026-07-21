from ..tools.macos import apps
from ..core.logging import logger
from ..utils.exceptions import SubprocessRunningError
from rich import print

import typer

app = typer.Typer()


@app.command("open", help="Open an application by name")
def open_command(name: list[str] = typer.Argument(..., help="Name of the app to open")):
    try:
        extract_name = " ".join(name)
        apps.open_app(app_name=extract_name)

    except SubprocessRunningError as err:
        logger.error(
            f"subprocess error:{err.message}",
            extra={
                "returncode": err.returncode,
                "stdout": err.stdout,
                "stderr": err.stderr,
            },
        )
        print("[bold red]can't get the app ❌[/bold red]try again!")
        typer.Exit()


@app.command("close", help="Close an application by name")
def close_command(
    name: list[str] = typer.Argument(..., help="Name of the app to close")
):
    try:
        extract_name = " ".join(name)
        apps.close_app(app_name=extract_name)

    except SubprocessRunningError as err:
        logger.error(
            f"subprocess error:{err.message}",
            extra={
                "returncode": err.returncode,
                "stdout": err.stdout,
                "stderr": err.stderr,
            },
        )
        print("[bold red]can't get the app  ❌[/bold red]try again!")
        typer.Exit()


@app.command("hide", help="Hide an application by name")
def hide_command(name: list[str] = typer.Argument(..., help="Name of the app to hide")):
    try:
        extract_name = " ".join(name)
        apps.hide_app(app_name=extract_name)

    except SubprocessRunningError as err:
        logger.error(
            f"subprocess error:{err.message}",
            extra={
                "returncode": err.returncode,
                "stdout": err.stdout,
                "stderr": err.stderr,
            },
        )
        print("[bold red]can't get the app  ❌[/bold red]try again!")
        typer.Exit()


@app.command("unhide", help="Unhide an application by name")
def unhide_command(
    name: list[str] = typer.Argument(..., help="Name of the app to unhide")
):
    try:
        extract_name = " ".join(name)
        apps.unhide_app(app_name=extract_name)

    except SubprocessRunningError as err:
        logger.error(
            f"subprocess error:{err.message}",
            extra={
                "returncode": err.returncode,
                "stdout": err.stdout,
                "stderr": err.stderr,
            },
        )
        print("[bold red]can't get the app  ❌[/bold red]try again!")
        typer.Exit()
