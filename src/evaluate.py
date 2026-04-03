#  imports json for metric file saving.
import json

#  imports model evaluation metrics.
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

#  imports the metrics file path.
from src.config import METRICS_FILE_PATH

#  imports the logger helper.
from src.logger import get_logger

#  imports the custom exception class.
from src.custom_exception import ProjectException

#  creates a logger for this module.
logger = get_logger(__name__)

# This function evaluates the model on the test set.
def evaluate_model(model, x_test, y_test):
    #  starts protected execution.
    try:
        #  logs evaluation start.
        logger.info("Model evaluation started.")

        #  creates predictions for the test data.
        predictions = model.predict(x_test)

        #  builds a dictionary of evaluation metrics.
        metrics = {
            "accuracy": float(accuracy_score(y_test, predictions)),
            "precision": float(precision_score(y_test, predictions)),
            "recall": float(recall_score(y_test, predictions)),
            "f1_score": float(f1_score(y_test, predictions)),
            "confusion_matrix": confusion_matrix(y_test, predictions).tolist(),
        }

        #  opens the metrics file for writing.
        with open(METRICS_FILE_PATH, "w", encoding="utf-8") as file:
            #  writes the metrics dictionary into JSON format.
            json.dump(metrics, file, indent=4)

        #  logs successful evaluation.
        logger.info("Model evaluation completed.")

        #  returns the metrics dictionary.
        return metrics

    # This block handles evaluation errors.
    except Exception as exc:
        #  logs the error.
        logger.error("Model evaluation failed.")

        #  raises a project specific exception.
        raise ProjectException(f"Failed to evaluate model: {exc}")