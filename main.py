from cli.commands.app import app as my_cli_app
from cli.core.logging import my_logger


def main():
    my_logger.info("Application starting")
    try:
        my_logger.info("Starting CLI app")
        my_cli_app()

    except KeyboardInterrupt:
        my_logger.warning("Application interrupted by user")
        raise

    except Exception:
        my_logger.exception("Application failed")
        raise
    finally:
        my_logger.info("Application stopped")


if __name__ == "__main__":
    main()
