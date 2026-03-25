# This line imports streamlit for the web app
import streamlit as st

# This line imports the prediction function
from src.predict import predict_loan_status

# This line sets the page title and layout
st.set_page_config(page_title="Loan Eligibility Prediction", layout="centered")

# This line shows the app title
st.title("Loan Eligibility Prediction App")

# This line shows a short description
st.write("Enter applicant details to predict loan approval status.")

# This line creates a dropdown for gender
gender = st.selectbox("Gender", ["Male", "Female"])

# This line creates a dropdown for marital status
married = st.selectbox("Married", ["Yes", "No"])

# This line creates a dropdown for number of dependents
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])

# This line creates a dropdown for education
education = st.selectbox("Education", ["Graduate", "Not Graduate"])

# This line creates a dropdown for self employment
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

# This line creates a numeric input for applicant income
applicant_income = st.number_input("Applicant Income", min_value=0.0, value=5000.0)

# This line creates a numeric input for coapplicant income
coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0, value=0.0)

# This line creates a numeric input for loan amount
loan_amount = st.number_input("Loan Amount", min_value=0.0, value=120.0)

# This line creates a numeric input for loan amount term
loan_amount_term = st.number_input("Loan Amount Term", min_value=0.0, value=360.0)

# This line creates a dropdown for credit history
credit_history = st.selectbox("Credit History", [1.0, 0.0])

# This line creates a dropdown for property area
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# This line checks if the Predict button is clicked
if st.button("Predict"):
    # This line creates a dictionary of user input
    user_input = {
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_amount_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }

    # This line starts a try block for safe prediction
    try:
        # This line gets the prediction result
        result = predict_loan_status(user_input)

        # This line displays the prediction result
        st.success(f"Prediction Result: {result}")

    # This block shows error messages in the app
    except Exception as exc:
        # This line displays the error
        st.error(f"Prediction failed: {exc}")