from cli.core.logging import logger
from cli.commands.app import app as my_cli_app


def main():
    logger.info("Application starting")
    try:
        logger.info("Starting CLI app")
        my_cli_app()
    except KeyboardInterrupt:
        logger.warning("Application interrupted by user")
        raise
    except Exception:
        logger.exception("Application failed")
        raise
    finally:
        logger.info("Application stopped")


if __name__ == "__main__":
    main()
