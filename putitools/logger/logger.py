import logging
from pathlib import Path

from rich.logging import RichHandler

LOG_PATH = Path("/tmp/my_logger.log")
logger = logging.getLogger(__name__)

# Split between shell and file
shell_handler = RichHandler()
file_handler = logging.FileHandler(LOG_PATH)

# Set different levels for the handlers
logger.setLevel(logging.DEBUG)
shell_handler.setLevel(logging.WARN)
file_handler.setLevel(logging.DEBUG)

# Define formatters
fmt_shell = "%(message)s"
fmt_file = (
    "[%(asctime)s][%(levelname)s][%(filename)s][%(module)s.%(funcName)s:%(lineno)d] %(message)s"
)
shell_formatter = logging.Formatter(fmt_shell)
file_formatter = logging.Formatter(fmt_file)

# Set formatters and add handlers
shell_handler.setFormatter(shell_formatter)
file_handler.setFormatter(file_formatter)

logger.addHandler(shell_handler)
logger.addHandler(file_handler)
