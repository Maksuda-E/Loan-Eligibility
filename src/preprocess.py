# This line imports pandas for data processing
import pandas as pd

# This line imports train_test_split for splitting the dataset
from sklearn.model_selection import train_test_split

# This line imports configuration values
from src.config import TEST_SIZE, RANDOM_STATE

# This line imports the logger
from src.logger import get_logger

# This line imports the custom exception
from src.custom_exception import ProjectException

# This line creates a logger for this file
logger = get_logger(__name__)

# This function cleans the dataset
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # This line starts the try block
    try:
        # This line logs the start of data cleaning
        logger.info("Starting data cleaning")

        # This line creates a copy of the dataset to avoid changing the original
        df = df.copy()

        # This line fills missing values in Gender with Male
        df["Gender"] = df["Gender"].fillna("Male")

        # This line fills missing values in Married with the mode
        df["Married"] = df["Married"].fillna(df["Married"].mode()[0])

        # This line fills missing values in Dependents with the mode
        df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])

        # This line fills missing values in Self_Employed with the mode
        df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])

        # This line fills missing values in LoanAmount with the median
        df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].median())

        # This line fills missing values in Loan_Amount_Term with the mode
        df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].mode()[0])

        # This line fills missing values in Credit_History with the mode
        df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])

        # This line removes the Loan_ID column because it is not useful for training
        df = df.drop("Loan_ID", axis=1)

        # This line converts Loan_Approved values from text to numbers
        df["Loan_Approved"] = df["Loan_Approved"].replace({"Y": 1, "N": 0})

        # This line defines the categorical columns for encoding
        categorical_columns = [
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self_Employed",
            "Property_Area"
        ]

        # This line converts categorical columns into numeric dummy variables
        df = pd.get_dummies(df, columns=categorical_columns, dtype=int)

        # This line logs that data cleaning is complete
        logger.info("Data cleaning completed successfully")

        # This line returns the cleaned dataset
        return df

    # This block handles errors during cleaning
    except Exception as exc:
        # This line logs the error
        logger.error("Error occurred during data cleaning")

        # This line raises a custom error
        raise ProjectException(f"Failed to clean data: {exc}")

# This function separates features and target
def split_features_target(df: pd.DataFrame):
    # This line starts the try block
    try:
        # This line logs the start of feature and target split
        logger.info("Splitting features and target")

        # This line stores all columns except Loan_Approved in x
        x = df.drop("Loan_Approved", axis=1)

        # This line stores the Loan_Approved column in y
        y = df["Loan_Approved"]

        # This line returns x and y
        return x, y

    # This block handles split errors
    except Exception as exc:
        # This line logs the error
        logger.error("Error occurred while splitting features and target")

        # This line raises a custom exception
        raise ProjectException(f"Failed to split features and target: {exc}")

# This function splits the data into training and testing sets
def split_train_test(x, y):
    # This line starts the try block
    try:
        # This line logs the start of train and test split
        logger.info("Starting train test split")

        # This line splits x and y into training and test sets
        x_train, x_test, y_train, y_test = train_test_split(
            x,
            y,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE,
            stratify=y
        )

        # This line logs that splitting is complete
        logger.info("Train test split completed successfully")

        # This line returns the split data
        return x_train, x_test, y_train, y_test

    # This block handles splitting errors
    except Exception as exc:
        # This line logs the error
        logger.error("Error occurred during train test split")

        # This line raises a custom exception
        raise ProjectException(f"Failed to split train and test data: {exc}")