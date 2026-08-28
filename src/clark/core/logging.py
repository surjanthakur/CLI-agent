import logging
import os

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

dsn = os.getenv("SENTRY_DSN")
ENV = os.getenv("ENVIRONMENT", "development")
logs_level = getattr(
    logging,
    os.getenv("LOG_LEVEL", "INFO").upper(),
    logging.INFO,
)


# Only send logs to Sentry, disable terminal output
my_logger = logging.getLogger(__name__)
my_logger.setLevel(logs_level)
my_logger.addHandler(logging.NullHandler())


# sentry logs
def init_sentry_logs():
    """initialize sentry logs if env is production"""

    if ENV == "production" and dsn:

        # Configure Sentry Logging Integration
        sentry_logging = LoggingIntegration(
            level=logs_level,  # Capture logs at this level
            event_level=logging.ERROR,  # Send events for ERROR and above
        )

    sentry_sdk.init(
        dsn=dsn,
        send_default_pii=False,
        enable_logs=True,
        environment=ENV,
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
