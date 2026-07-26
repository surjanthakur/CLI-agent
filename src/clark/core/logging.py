import logging
import os

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

from .config import settings

# Configure Sentry Logging Integration
sentry_logging = LoggingIntegration(
    level=settings.LOGS_LEVEL,  # Capture logs at this level
    event_level=logging.ERROR,  # Send events for ERROR and above
)

sentry_sdk.init(
    dsn=settings.SENTRY_DNS,
    send_default_pii=False,
    enable_logs=True,
    environment=os.getenv("ENVIRONMENT", "production"),
    # Performance Monitoring
    traces_sample_rate=0.1,  # 10% of transactions for performance monitoring
    # Release tracking
    release=os.getenv("APP_VERSION", "unknown"),
    # Integrations
    integrations=[sentry_logging],
    # Error handling
    attach_stacktrace=True,  # Include stack traces
    max_breadcrumbs=50,  # Keep last 50 breadcrumbs
    # Debug mode
    debug=False,
    # Before send hook for filtering sensitive data
    before_send=lambda event, hint: event,
)

# Only send logs to Sentry, disable terminal output
my_logger = logging.getLogger(__name__)
my_logger.setLevel(settings.LOGS_LEVEL)
my_logger.addHandler(logging.NullHandler())
