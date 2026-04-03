#  imports the logging module.
import logging

#  imports the os module.
import os

#  imports the logs directory path.
from src.config import LOGS_DIR, LOG_FILE_PATH

#  creates the logs directory if it does not already exist.
os.makedirs(LOGS_DIR, exist_ok=True)

#  configures the base logger.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

# This function returns a logger object for a given name.
def get_logger(name: str):
    #  returns the logger.
    return logging.getLogger(name)