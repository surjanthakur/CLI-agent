from typing import Callable, Any

from ..tools.macos import apps
from ..core.logging import logger
from ..utils.exceptions import SubprocessRunningError

import typer

app = typer.Typer()


# exception handler
def handle_exceptions(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """Run a macOS apps helper function and handle subprocess failure gracefully.

    If the wrapped function raises a SubprocessRunningError, the error is logged with
    its return code, stdout, and stderr, and a Rich-styled error message is printed.
    """
    try:
        return func(*args, **kwargs)
    except SubprocessRunningError as err:
        logger.error(
            f"{err} stderr:{err.stderr} stdout:{err.stdout} return_code:{err.returncode}",
        )
        typer.echo(message=f"{err.stderr}", err=True)
        raise typer.Exit()


# opne app
@app.command("open", help="Open an application by name")
def open_command(name: list[str] = typer.Argument(..., help="Name of the app to open")):
    extract_name = " ".join(name)
    handle_exceptions(apps.open_app, extract_name)


# close app
@app.command("close", help="Close an application by name")
def close_command(
    name: list[str] = typer.Argument(..., help="Name of the app to close")
):
    extract_name = " ".join(name)
    handle_exceptions(apps.close_app, extract_name)


# hide app
@app.command("hide", help="Hide an application by name")
def hide_command(name: list[str] = typer.Argument(..., help="Name of the app to hide")):
    extract_name = " ".join(name)
    handle_exceptions(apps.hide_app, extract_name)


# unhide app
@app.command("unhide", help="Unhide an application by name")
def unhide_command(
    name: list[str] = typer.Argument(..., help="Name of the app to unhide")
):
    extract_name = " ".join(name)
    handle_exceptions(apps.unhide_app, extract_name)
