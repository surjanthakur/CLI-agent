from rich import print
from ..services.installer import install_brightness

import shutil
import typer

app = typer.Typer()


def ensure_homebrew():
    if shutil.which("brew"):
        return

    raise RuntimeError("Homebrew is required. Please install Homebrew first.")


def ensure_brightness():

    if shutil.which("brightness"):
        return

    print("Brightness support requires the 'brightness' utility.")

    answer = typer.confirm("Are you sure you want to install it?")

    if not answer:
        print("stoped downloading brightness...")
        raise typer.Abort()
    install_brightness()
