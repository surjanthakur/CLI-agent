import subprocess
from rich.console import Console

console = Console()


def install_brightness():
    """function install the brightness package in cli to automate mac brightness settings."""
    try:
        with console.status("[bold green]Installing brightness..."):
            process = subprocess.Popen(
                ["brew", "install", "brightness"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            stdout, stderr = process.communicate()

            if process.returncode != 0:
                raise RuntimeError(stderr)
            print(f"stdout {stdout}")

    except RuntimeError as err:
        print(f"error while running subprocess script: {err}")
