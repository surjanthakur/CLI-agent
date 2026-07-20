import subprocess
from rich import print


# run osascript in subprocess
def run_process(script: str):
    """
    this function run's the subprocess for osascript
    """
    try:
        process = subprocess.Popen(
            ["osascript", "-e", script],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(repr(stdout))
            raise RuntimeError(repr(stderr))

    except RuntimeError as err:
        print(f"error while running subprocess script: {err}")
