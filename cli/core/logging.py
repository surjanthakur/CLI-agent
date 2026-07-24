import logging

# import sentry_sdk

# from .config import settings

# sentry_sdk.init(
#     dsn=settings.SENTRY_DNS,
#     enable_logs=True,
# )

logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

my_logger = logging.getLogger(__name__)
