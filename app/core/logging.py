import logging
import sys

# Define the log format
# %(levelname)s: The severity (INFO, ERROR, etc.)
# %(asctime)s: Timestamp
# %(module)s: Which file the log came from
LOG_FORMAT = "%(levelname)s: %(asctime)s - %(module)s - %(message)s"

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        force=True ,
        # handlers=[
        #     logging.StreamHandler(sys.stdout) 
        # ]
    )
    return logging.getLogger("app")

logger = setup_logging()

