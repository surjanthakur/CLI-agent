from src.commands.app import app as my_cli_app
from src.core.logging import logger
from src.services import startup


def main():
    logger.info("Application starting")
    try:
        logger.info("Initializing startup services")
        startup.initialize()
        logger.info("Startup services initialized")

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
