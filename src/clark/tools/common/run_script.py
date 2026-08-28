import subprocess

from rich import print

from ...core.logging import my_logger


# run osascript process
def run_process(script: str, timeout: int = 15) -> str | None:
    """Run an AppleScript string and return its stdout.

    Returns None if execution fails or is unsupported.
    """

    try:
        my_logger.info("running subprocess...")

        process = subprocess.run(
            ["osascript", "-e", script],
            text=True,
            capture_output=True,
            check=False,
            timeout=timeout,
        )
        if process.returncode != 0:
            err_message = process.stderr.strip() or "Unknown AppleScript Error"
            my_logger.error(
                f"AppleScript error: (code {process.returncode}): {err_message}"
            )
            raise RuntimeError(f"application error: {err_message}\n")

        my_logger.info("AppleScript executed successfully.")

    except FileNotFoundError:
        my_logger.warning("osascript command not found. Are you on macOS?")
        return None

    except subprocess.TimeoutExpired:
        my_logger.error(f"AppleScript timedout after {timeout} seconds.")
        return None

    except RuntimeError:
        raise

    except Exception as err:  # noqa: BLE001
        my_logger.exception(f"Unexpected error running AppleScript: {err}")
        return None
    else:
        print("[bold blue]command executed successfully[/bold blue]\n")
        return process.stdout.strip()
