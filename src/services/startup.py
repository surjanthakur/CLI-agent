from ..utils.dependencies import ensure_homebrew, ensure_ollama


def initialize():
    "this fucnction checks the dependencies are installed or not"
    ensure_homebrew()
    ensure_ollama()
