from ..services.installer import download_ollama, download_llm_model
import shutil
import typer
import subprocess
import time

app = typer.Typer()


def ensure_ollama():
    "this function ensure the ollama is installed"
    if shutil.which("ollama"):
        return  # Model already exists
    download_ollama()  # downloading ollama


# starting ollama server
def start_ollama_server():
    subprocess.Popen(
        ["ollama", "serve"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(3)


# check is server running ?
def is_ollama_running() -> bool:
    try:
        subprocess.run(
            ["ollama", "list"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


# check is qwen2.5-coder installed ?
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
        if not is_ollama_running():  # if not running
            start_ollama_server()  # start the ollama server
            download_llm_model()  # download the model
