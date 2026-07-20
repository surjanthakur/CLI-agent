from src.commands.app import app as my_cli_app
from src.services import startup


def main():
    startup.initialize()
    my_cli_app()


if __name__ == "__main__":
    main()
