#  imports os for directory creation.
import os

#  imports pickle for saving artifacts.
import pickle

#  imports LogisticRegression.
from sklearn.linear_model import LogisticRegression

#  imports MinMaxScaler.
from sklearn.preprocessing import MinMaxScaler

#  imports Pipeline for chaining preprocessing and model steps.
from sklearn.pipeline import Pipeline

#  imports project configuration values.
from src.config import ARTIFACTS_DIR, MODEL_FILE_PATH, FEATURE_COLUMNS_FILE_PATH, RANDOM_STATE

#  imports the logger helper.
from src.logger import get_logger

#  imports the custom exception class.
from src.custom_exception import ProjectException

#  creates a logger for this module.
logger = get_logger(__name__)

# This function trains the logistic regression model.
def train_model(x_train, y_train):
    #  starts protected execution.
    try:
        #  logs the training start.
        logger.info("Model training started.")

        #  creates a pipeline with scaling and logistic regression.
        model = Pipeline(
            steps=[
                ("scaler", MinMaxScaler()),
                ("classifier", LogisticRegression(random_state=RANDOM_STATE, max_iter=1000)),
            ]
        )

        #  trains the pipeline on the training data.
        model.fit(x_train, y_train)

        #  logs training success.
        logger.info("Model training completed.")

        #  returns the trained model.
        return model

    # This block handles training errors.
    except Exception as exc:
        #  logs the error.
        logger.error("Model training failed.")

        #  raises a project specific exception.
        raise ProjectException(f"Failed to train model: {exc}")

# This function saves the trained model and feature list.
def save_artifacts(model, feature_columns):
    #  starts protected execution.
    try:
        #  creates the artifacts directory.
        os.makedirs(ARTIFACTS_DIR, exist_ok=True)

        #  opens the model file in binary write mode.
        with open(MODEL_FILE_PATH, "wb") as model_file:
            #  saves the trained model.
            pickle.dump(model, model_file)

        #  opens the feature list file in binary write mode.
        with open(FEATURE_COLUMNS_FILE_PATH, "wb") as feature_file:
            #  saves the feature column names.
            pickle.dump(feature_columns, feature_file)

        #  logs successful artifact saving.
        logger.info("Artifacts saved successfully.")

    # This block handles saving errors.
    except Exception as exc:
        #  logs the error.
        logger.error("Saving artifacts failed.")

        #  raises a project specific exception.
        raise ProjectException(f"Failed to save artifacts: {exc}")