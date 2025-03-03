# backend/app/utils/logger.py
import logging
import sys

def setup_logger(name: str) -> logging.Logger:
    """
    Configure and return a logger with a specified name.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(name)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Example: create a logger instance for the app
logger = setup_logger("app")
