import shutil
import typer

app = typer.Typer()


def ensure_homebrew():
    """function ensure the homebrew is install in your mac terminal"""
    if shutil.which("brew"):
        return

    raise RuntimeError("Homebrew is required. Please install Homebrew first.")
