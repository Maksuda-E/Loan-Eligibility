#  imports pandas for preprocessing.
import pandas as pd

#  imports the train test split function.
from sklearn.model_selection import train_test_split

#  imports configuration values.
from src.config import TEST_SIZE, RANDOM_STATE

#  imports the logger helper.
from src.logger import get_logger

#  imports the custom exception class.
from src.custom_exception import ProjectException

#  creates a logger for this module.
logger = get_logger(__name__)

# This function cleans and encodes the dataset.
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    #  starts protected execution.
    try:
        #  logs the start of preprocessing.
        logger.info("Starting data preprocessing.")

        #  creates a copy of the input data.
        df = df.copy()

        #  fills missing values in Gender with Male.
        df["Gender"] = df["Gender"].fillna("Male")

        #  fills missing values in Married with the mode.
        df["Married"] = df["Married"].fillna(df["Married"].mode()[0])

        #  fills missing values in Dependents with the mode.
        df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])

        #  fills missing values in Self_Employed with the mode.
        df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])

        #  fills missing values in LoanAmount with the median.
        df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].median())

        #  fills missing values in Loan_Amount_Term with the mode.
        df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].mode()[0])

        #  fills missing values in Credit_History with the mode.
        df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])

        #  drops Loan_ID because it is not predictive.
        df = df.drop("Loan_ID", axis=1)

        #  converts the target column from labels to numeric values.
        df["Loan_Approved"] = df["Loan_Approved"].replace({"Y": 1, "N": 0}).astype(int)

        #  defines categorical columns for one hot encoding.
        categorical_columns = [
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self_Employed",
            "Property_Area",
        ]

        #  creates dummy variables for the categorical columns.
        df = pd.get_dummies(df, columns=categorical_columns, dtype=int)

        #  logs successful preprocessing.
        logger.info("Data preprocessing completed.")

        #  returns the cleaned DataFrame.
        return df

    # This block handles preprocessing errors.
    except Exception as exc:
        #  logs the error.
        logger.error("Preprocessing failed.")

        #  raises a project specific exception.
        raise ProjectException(f"Failed to clean data: {exc}")

# This function separates feature columns from the target column.
def split_features_target(df: pd.DataFrame):
    #  starts protected execution.
    try:
        #  logs the split action.
        logger.info("Splitting features and target.")

        #  stores all input features.
        x = df.drop("Loan_Approved", axis=1)

        #  stores the target column.
        y = df["Loan_Approved"]

        #  returns features and target.
        return x, y

    # This block handles split errors.
    except Exception as exc:
        #  logs the error.
        logger.error("Feature target split failed.")

        #  raises a project specific exception.
        raise ProjectException(f"Failed to split features and target: {exc}")

# This function splits the data into training and testing sets.
def split_train_test(x, y):
    #  starts protected execution.
    try:
        #  logs the train test split action.
        logger.info("Creating train and test datasets.")

        #  creates the train and test sets.
        x_train, x_test, y_train, y_test = train_test_split(
            x,
            y,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE,
            stratify=y,
        )

        #  logs successful splitting.
        logger.info("Train test split completed.")

        #  returns the split datasets.
        return x_train, x_test, y_train, y_test

    # This block handles splitting errors.
    except Exception as exc:
        #  logs the error.
        logger.error("Train test split failed.")

        #  raises a project specific exception.
        raise ProjectException(f"Failed to split train and test data: {exc}")