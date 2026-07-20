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
            print(f"[bold red]✗ Process Error:[/bold red] {repr(stderr)}")
    except subprocess.CalledProcessError as err:
        print(f"[bold red]✗ Error:[/bold red] {err}")
