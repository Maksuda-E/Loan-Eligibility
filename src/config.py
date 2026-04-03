#  imports the os module for path handling.
import os

#  gets the absolute path of the current file.
CURRENT_FILE_PATH = os.path.abspath(__file__)

#  gets the src directory path.
SRC_DIR = os.path.dirname(CURRENT_FILE_PATH)

#  gets the project root directory path.
PROJECT_DIR = os.path.dirname(SRC_DIR)

#  builds the data folder path.
DATA_DIR = os.path.join(PROJECT_DIR, "data")

#  builds the artifacts folder path.
ARTIFACTS_DIR = os.path.join(PROJECT_DIR, "artifacts")

#  builds the logs folder path.
LOGS_DIR = os.path.join(PROJECT_DIR, "logs")

#  builds the raw dataset path.
DATA_FILE_PATH = os.path.join(DATA_DIR, "credit.csv")

#  builds the trained model file path.
MODEL_FILE_PATH = os.path.join(ARTIFACTS_DIR, "loan_model.pkl")

#  builds the feature columns file path.
FEATURE_COLUMNS_FILE_PATH = os.path.join(ARTIFACTS_DIR, "feature_columns.pkl")

#  builds the metrics file path.
METRICS_FILE_PATH = os.path.join(ARTIFACTS_DIR, "metrics.json")

#  builds the log file path.
LOG_FILE_PATH = os.path.join(LOGS_DIR, "project.log")

#  sets a fixed random state for reproducibility.
RANDOM_STATE = 42

#  sets the test split size.
TEST_SIZE = 0.20