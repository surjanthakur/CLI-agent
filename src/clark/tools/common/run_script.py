import logging
import subprocess

from rich import print

logger = logging.getLogger(__name__)


# run osascript in subprocess
def run_process(script: str):
    """
    Run an AppleScript and return its output (stdout).
    """

    try:
        process = subprocess.run(
            ["osascript", "-e", script],
            text=True,
            capture_output=True,
            check=False,
        )
        if process.returncode != 0:
            err_message = process.stderr.strip() or "Unknown AppleScript Error"
            logger.error(
                f"AppleScript error: (code {process.returncode}): {err_message}"
            )
            raise RuntimeError(f"application error: {err_message}\n")

    except FileNotFoundError:
        logger.warning("osascript command not found. Are you on macOS?")
        print("[red]osascript not found. This only works on macOS.[/red]\n")
        return None  # noqa: RET501

    except TimeoutError:
        logger.warning("Timeout error while running subprocess osascript")
        print("[red]takes too much time to run check internet!\n")

    except RuntimeError:
        logger.warning(f"wrong command name: {process.stderr.strip()}")
        print(f"[red]{process.stderr.strip()}[/red]\n")

    except Exception:
        logger.exception("Unexpected error on running AppleScript")
        print("[red]Something went wrong while running this command.[/red]\n")
        return None  # noqa: RET501
    else:
        print("[bold blue]command executed successfully[/bold blue]\n")
