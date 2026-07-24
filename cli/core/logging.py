import logging
from logging.handlers import SysLogHandler

from ..core.config import settings

logging.basicConfig(
    filename="app.log",
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

handler = SysLogHandler(address=(settings.PAPERTRAIL_HOST, settings.PAPERTRAIL_TOKEN))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
