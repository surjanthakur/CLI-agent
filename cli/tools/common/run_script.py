import subprocess
from ...core.logging import logger

from rich import print


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
            err_message = process.stderr().strip() or "Unknown AppleScript Error"
            logger.error(
                f"AppleScript error: (code {process.returncode}): {err_message}"
            )
            raise RuntimeError(f"application error: {err_message}")

    except FileNotFoundError:
        logger.warning("osascript command not found. Are you on macOS?")
        print("[red]osascript not found. This only works on macOS.[/red]")
        return None

    except TimeoutError:
        logger.warning("Timeout error while running subprocess osascript")
        print("[red]takes too much time to run check internet!")

    except Exception as err:
        logger.exception(f"Unexpected error running AppleScript: {err}")
        print("[red]Something went wrong while running the command.[/red]")
        return None
