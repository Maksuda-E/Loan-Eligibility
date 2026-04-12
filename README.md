# Loan Eligibility Prediction using Machine Learning
# Overview

This project converts the Loan Eligibility notebook into a modular Python project and an interactive Streamlit web application.

The goal is to predict whether a loan application will be approved or not using a classification model.

The project follows the notebook workflow:

Handle missing values using mode and median
Perform data preprocessing and feature engineering
Apply one-hot encoding for categorical variables
Scale features using MinMaxScaler
Train classification models (Logistic Regression, Decision Tree, Random Forest)
Evaluate performance using classification metrics
Select best model based on accuracy
Deploy model using Streamlit web application
Problem Statement

Banks receive a large number of loan applications.

Not all applicants are eligible, and approving the wrong loan can lead to financial risk.

Using machine learning, we predict whether a loan should be:

Approved
Not Approved

based on applicant details such as income, credit history, and property information.

# Dataset

The dataset contains the following features:

Loan_ID: Unique applicant ID

Gender: Male/Female

Married: Yes/No

Dependents: Number of dependents

Education: Graduate/Not Graduate

Self_Employed: Yes/No

ApplicantIncome: Applicant’s monthly income

CoapplicantIncome: Co-applicant’s income

LoanAmount: Loan amount requested

Loan_Amount_Term: Loan repayment term

Credit_History: Credit history (1 or 0)

Property_Area: Urban/Semiurban/Rural

Loan_Approved: Target variable (Y/N)

Dataset file:
data/credit.csv

# Model Workflow
Load dataset

Handle missing values:

Categorical → Mode

Numerical → Median

Drop unnecessary column:

Loan_ID

Convert target variable:
Y → 1
N → 0

Apply one-hot encoding for categorical variables

Split data into train and test sets

Scale features using MinMaxScaler

# Train models:
Logistic Regression

Decision Tree

Random Forest

# Evaluate models using:
Accuracy

Confusion Matrix

Select best model (Logistic Regression)

Save model and artifacts

Use model in Streamlit app for prediction

# Model Performance
Logistic Regression Accuracy: ~80.4%

Random Forest Accuracy: ~78%

Decision Tree Accuracy: ~69%

The Logistic Regression model performs best and meets the required accuracy (>76%).

Prediction Interpretation

The model classifies loan applications into:

Approved (1)
Not Approved (0)

The prediction is based on applicant financial and demographic features.

# How to Run
Install dependencies

pip install -r requirements.txt

# Run training pipeline

python main.py

# Run Streamlit app

streamlit run app.py

# Streamlit Link
https://loan-eligibility-maksuda.streamlit.app/

# Key Features
Modular code structure
Logging and exception handling
Multiple model training and comparison
Proper preprocessing pipeline
Model evaluation using classification metrics
Interactive Streamlit web application

## Project Structure
```text
Loan-Eligibility/
│
├── app.py  
├── main.py  
├── requirements.txt  
├── runtime.txt  
├── README.md  
│  
├── data/  
│   └── credit.csv  
│  
├── artifacts/  
│   ├── loan_model.pkl  
│   ├── feature_columns.pkl  
│   └── metrics.json  
│  
├── logs/  
│   └── project.log  
│  
└── src/  
    ├── __init__.py  
    ├── config.py  
    ├── custom_exception.py  
    ├── data_loader.py  
    ├── evaluate.py  
    ├── logger.py  
    ├── preprocessing.py  
    ├── train.py  
    └── predict.py  
