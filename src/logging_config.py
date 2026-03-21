import logging
import sys
import structlog


def configure_logging():
    """
    Configure structlog for better structured logging.
    This works by wrapping standard Python logging.
    """
    
    # 1. Standard Python Logging configuration (used for internal/library logs)
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.INFO,
    )

    # 2. Structlog configuration
    structlog.configure(
        processors=[
            # If log level of event is lower than level, skip
            structlog.stdlib.filter_by_level,
            # Add the name of the logger to event dict.
            structlog.stdlib.add_logger_name,
            # Add log level to event dict.
            structlog.stdlib.add_log_level,
            # Perform %-style formatting.
            structlog.stdlib.PositionalArgumentsFormatter(),
            # Add a timestamp in ISO format.
            structlog.processors.TimeStamper(fmt="iso"),
            # If the "stack_info" key is present, add stack information.
            structlog.processors.StackInfoRenderer(),
            # If some value is an Exception, format it.
            structlog.processors.format_exc_info,
            # Render the final output as JSON (for analytics/production)
            # or as a pretty string (for development/debugging)
            structlog.dev.ConsoleRenderer() if sys.stdout.isatty() else structlog.processors.JSONRenderer(),
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

def get_logger(name: str):
    """Utility to get a logger."""
    return structlog.get_logger(name)
