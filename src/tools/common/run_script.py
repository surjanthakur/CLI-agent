import subprocess
from ...utils.exceptions import SubprocessRunningError


# run osascript in subprocess
def run_process(script: str):
    """
    this function run's the subprocess for osascript
    """
    process = subprocess.run(
        ["osascript", "-e", script], text=True, capture_output=True
    )
    if process.returncode != 0:
        message = (repr(process.stderr)) or "Failed to execute AppleScript."
        raise SubprocessRunningError(
            message,
            returncode=process.returncode,
            stdout=process.stdout,
            stderr=process.stderr,
        )
