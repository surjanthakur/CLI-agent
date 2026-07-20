from ..utils.dependencies import ensure_brightness, ensure_homebrew


def initialize():
    "this fucnction checks the dependencies are installed or not"
    ensure_homebrew()
    ensure_brightness()
