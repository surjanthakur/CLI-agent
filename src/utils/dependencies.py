import shutil
import typer
import subprocess

app = typer.Typer()


def ensure_homebrew():
    """this function ensure the homebrew is installed"""
    if shutil.which("brew"):
        return
    raise RuntimeError("Homebrew is required. Please installed Homebrew first.")


def ensure_ollama():
    "this function ensure the ollama is installed"
    if shutil.which("ollama"):
        return  # Model already exists
    print("model installing")


def ensure_llm_model():
    "this function ensure the model qwen2.5 coder is installed"
    try:
        subprocess.run(
            ["ollama", "show", "qwen2.5-coder:3b"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return  # Model already exists

    except (subprocess.CalledProcessError, FileNotFoundError):
        print("installing model")
