#  imports pandas for CSV loading.
import pandas as pd

#  imports the logger helper.
from src.logger import get_logger

#  imports the custom exception.
from src.custom_exception import ProjectException

#  creates a logger for this module.
logger = get_logger(__name__)

# This function loads the dataset from a CSV file.
def load_data(file_path: str) -> pd.DataFrame:
    #  starts protected execution.
    try:
        #  logs the file loading start.
        logger.info("Loading dataset from %s", file_path)

        #  reads the CSV file into a DataFrame.
        df = pd.read_csv(file_path)

        #  logs successful loading.
        logger.info("Dataset loaded successfully with shape %s", df.shape)

        #  returns the loaded DataFrame.
        return df

    # This block handles file loading errors.
    except Exception as exc:
        #  logs the error.
        logger.error("Failed to load dataset.")

        #  raises a project specific exception.
        raise ProjectException(f"Failed to load data: {exc}")