#  imports pickle for loading saved artifacts.
import pickle

#  imports pandas for input preparation.
import pandas as pd

#  imports artifact paths from the config file.
from src.config import MODEL_FILE_PATH, FEATURE_COLUMNS_FILE_PATH

#  imports the logger helper.
from src.logger import get_logger

#  imports the custom exception class.
from src.custom_exception import ProjectException

#  creates a logger for this module.
logger = get_logger(__name__)

# This function loads the trained model and saved feature list.
def load_model_and_features():
    #  starts protected execution.
    try:
        #  opens the saved model file.
        with open(MODEL_FILE_PATH, "rb") as model_file:
            #  loads the trained model.
            model = pickle.load(model_file)

        #  opens the saved feature list file.
        with open(FEATURE_COLUMNS_FILE_PATH, "rb") as feature_file:
            #  loads the feature columns.
            feature_columns = pickle.load(feature_file)

        #  logs successful loading.
        logger.info("Model artifacts loaded successfully.")

        #  returns the model and feature list.
        return model, feature_columns

    # This block handles loading errors.
    except Exception as exc:
        #  logs the error.
        logger.error("Loading model artifacts failed.")

        #  raises a project specific exception.
        raise ProjectException(f"Failed to load model artifacts: {exc}")

# This function converts a user input dictionary into a model ready DataFrame.
def prepare_input_data(user_input: dict, feature_columns: list):
    #  starts protected execution.
    try:
        #  converts the input dictionary into a one row DataFrame.
        input_df = pd.DataFrame([user_input])

        #  applies one hot encoding to categorical values.
        input_df = pd.get_dummies(input_df, dtype=int)

        #  reorders the columns to match the training feature order.
        input_df = input_df.reindex(columns=feature_columns, fill_value=0)

        #  returns the prepared input DataFrame.
        return input_df

    # This block handles input preparation errors.
    except Exception as exc:
        #  logs the error.
        logger.error("Preparing input data failed.")

        #  raises a project specific exception.
        raise ProjectException(f"Failed to prepare input data: {exc}")

# This function predicts the loan status from user input.
def predict_loan_status(user_input: dict):
    #  starts protected execution.
    try:
        #  loads the model and feature names.
        model, feature_columns = load_model_and_features()

        #  prepares the user input for prediction.
        input_df = prepare_input_data(user_input, feature_columns)

        #  generates the model prediction.
        prediction = model.predict(input_df)[0]

        #  returns the approved label when prediction is positive.
        if prediction == 1:
            return "Approved"

        #  returns the negative label when prediction is zero.
        return "Not Approved"

    # This block handles prediction errors.
    except Exception as exc:
        #  logs the error.
        logger.error("Prediction failed.")

        #  raises a project specific exception.
        raise ProjectException(f"Failed to predict loan status: {exc}")