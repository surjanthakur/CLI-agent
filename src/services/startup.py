from ..utils.dependencies import ensure_homebrew, ensure_ollama, ensure_llm_model


def initialize():
    "this fucnction checks the dependencies are installed or not"
    ensure_homebrew()
    ensure_ollama()
    ensure_llm_model()
