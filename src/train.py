# This line imports os for folder creation
import os

# This line imports pickle for saving the model
import pickle

# This line imports LogisticRegression as the classifier
from sklearn.linear_model import LogisticRegression

# This line imports MinMaxScaler for feature scaling
from sklearn.preprocessing import MinMaxScaler

# This line imports Pipeline for combining scaler and model
from sklearn.pipeline import Pipeline

# This line imports config values
from src.config import ARTIFACTS_DIR, MODEL_FILE_PATH, FEATURE_COLUMNS_FILE_PATH, RANDOM_STATE

# This line imports the logger
from src.logger import get_logger

# This line imports the custom exception
from src.custom_exception import ProjectException

# This line creates a logger for this file
logger = get_logger(__name__)

# This function trains the model
def train_model(x_train, y_train):
    # This line starts the try block
    try:
        # This line logs the start of model training
        logger.info("Model training started")

        # This line creates a pipeline with scaling and logistic regression
        model = Pipeline(
            steps=[
                ("scaler", MinMaxScaler()),
                ("classifier", LogisticRegression(random_state=RANDOM_STATE, max_iter=1000))
            ]
        )

        # This line trains the model on the training data
        model.fit(x_train, y_train)

        # This line logs that training has completed
        logger.info("Model training completed successfully")

        # This line returns the trained model
        return model

    # This block handles training errors
    except Exception as exc:
        # This line logs the error
        logger.error("Error occurred during model training")

        # This line raises a custom exception
        raise ProjectException(f"Failed to train model: {exc}")

# This function saves the model and feature columns
def save_artifacts(model, feature_columns):
    # This line starts the try block
    try:
        # This line creates the artifacts folder if it does not exist
        os.makedirs(ARTIFACTS_DIR, exist_ok=True)

        # This line opens the model file in write binary mode
        with open(MODEL_FILE_PATH, "wb") as model_file:
            # This line saves the trained model
            pickle.dump(model, model_file)

        # This line opens the feature columns file in write binary mode
        with open(FEATURE_COLUMNS_FILE_PATH, "wb") as feature_file:
            # This line saves the feature columns
            pickle.dump(feature_columns, feature_file)

        # This line logs that artifacts were saved successfully
        logger.info("Artifacts saved successfully")

    # This block handles save errors
    except Exception as exc:
        # This line logs the error
        logger.error("Error occurred while saving artifacts")

        # This line raises a custom exception
        raise ProjectException(f"Failed to save artifacts: {exc}")