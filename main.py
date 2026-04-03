#  imports the dataset path from the configuration file.
from src.config import DATA_FILE_PATH

#  imports the data loading function.
from src.data_loader import load_data

#  imports preprocessing helper functions.
from src.preprocessing import clean_data, split_features_target, split_train_test

#  imports the model training and artifact saving functions.
from src.train import train_model, save_artifacts

#  imports the evaluation function.
from src.evaluate import evaluate_model

#  imports the logger generator.
from src.logger import get_logger

#  creates a logger object for the current file.
logger = get_logger(__name__)

# This function runs the full training pipeline.
def main():
    #  logs the start of the pipeline.
    logger.info("Training pipeline started.")

    #  loads the raw dataset.
    df = load_data(DATA_FILE_PATH)

    #  cleans and prepares the dataset.
    df_clean = clean_data(df)

    #  separates features and target.
    x, y = split_features_target(df_clean)

    #  splits the dataset into train and test sets.
    x_train, x_test, y_train, y_test = split_train_test(x, y)

    #  trains the model.
    model = train_model(x_train, y_train)

    #  saves the trained model and feature names.
    save_artifacts(model, list(x.columns))

    #  evaluates the trained model on the test set.
    metrics = evaluate_model(model, x_test, y_test)

    #  prints a success message to the terminal.
    print("Training completed successfully.")

    #  prints the evaluation heading.
    print("Evaluation metrics:")

    #  loops through each metric.
    for key, value in metrics.items():
        #  prints the metric name and metric value.
        print(f"{key}: {value}")

    #  logs the successful completion of the pipeline.
    logger.info("Training pipeline completed.")

#  checks whether the file is executed directly.
if __name__ == "__main__":
    #  starts the main pipeline.
    main()