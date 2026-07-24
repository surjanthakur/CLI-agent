import logging

import sentry_sdk

from .config import settings

sentry_sdk.init(
    dsn=settings.SENTRY_DNS,
    send_default_pii=True,
)

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
