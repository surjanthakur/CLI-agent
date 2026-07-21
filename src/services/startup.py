from ..utils.dependencies import ensure_ollama, ensure_llm_model


def initialize():
    "this fucnction checks the dependencies are installed or not"
    ensure_ollama()
    ensure_llm_model()
