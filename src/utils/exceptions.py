from typing import Callable, Any
from ..core.logging import logger
import typer


class SubprocessRunningError(Exception):
    """Raised when an osascript subprocess fails."""

    def __init__(
        self,
        message: str,
        *,
        returncode: int | None = None,
        stdout: str = "",
        stderr: str = "",
    ):
        super().__init__(message)
        self.message = message
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


# helper func
def handle_exceptions(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """helper function and handle subprocess failure gracefully.

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
        raise typer.Abort()
