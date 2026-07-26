import subprocess

from rich import print

from ...core.logging import my_logger


# run osascript in subprocess
def run_process(script: str):
    """
    Run an AppleScript and return its output (stdout).
    """

    try:
        my_logger.info("running subprocess...")

        process = subprocess.run(
            ["osascript", "-e", script],
            text=True,
            capture_output=True,
            check=False,
        )
        if process.returncode != 0:
            err_message = process.stderr.strip().title() or "Unknown AppleScript Error"
            my_logger.error(
                f"AppleScript error: (code {process.returncode}): {err_message}"
            )
            raise RuntimeError(f"application error: {err_message}\n")

        my_logger.info("end subprocess...")

    except FileNotFoundError:
        my_logger.warning("osascript command not found. Are you on macOS?")
        print("[red]osascript not found. This only works on macOS.[/red]\n")
        return None  # noqa: RET501

    except TimeoutError:
        my_logger.warning("Timeout error while running subprocess osascript")
        print("[red]takes too much time to run check internet!\n")

    except RuntimeError:
        my_logger.warning(f"wrong command name: {process.stderr.strip()}")
        print(f"[red]{process.stderr.strip()}[/red]\n")

    except Exception:  # noqa: BLE001
        my_logger.exception("Unexpected error on running AppleScript")
        print("[red]Something went wrong while running this command.[/red]\n")
        return None  # noqa: RET501
    else:
        print("[bold blue]command executed successfully[/bold blue]\n")
