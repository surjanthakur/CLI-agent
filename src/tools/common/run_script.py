import subprocess
from ...utils.exceptions import SubprocessRunningError
from ...core.logging import logger


# run osascript in subprocess
def run_process(script: str):
    """
    this function run's the subprocess for osascript
    """
    process = subprocess.run(
        ["osascript", "-e", script], text=True, capture_output=True
    )
    if process.returncode != 0:
        raise SubprocessRunningError(
            "Failed to execute AppleScript.",
            returncode=process.returncode,
            stdout=process.stdout,
            stderr=process.stderr,
        )
