# This line imports Streamlit for building the web app.
import streamlit as st

# This line imports the prediction function from your pipeline.
from src.predict import predict_loan_status


# This line sets basic page configuration such as title and layout.
st.set_page_config(page_title="Loan Eligibility", layout="wide")


# This block injects custom CSS to improve UI appearance.
st.markdown(
    """
    <style>

        /* REMOVE STREAMLIT HEADER */
        header {visibility: hidden;}

        /* REMOVE TOP WHITE SPACE */
        .block-container {
            padding-top: 1rem !important;
        }

        .stApp > div:first-child {
            padding-top: 0rem;
        }

        /* BACKGROUND COLOR */
        .stApp {
            background-color: #f5f7fa;
        }

        /* CARD STYLE */
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }

        /* BUTTON STYLE */
        div.stButton > button {
            background-color: #2563eb;
            color: white;
            border-radius: 8px;
            height: 45px;
            font-size: 16px;
            font-weight: 600;
            border: none;
            width: 100%;
        }

        div.stButton > button:hover {
            background-color: #1d4ed8;
            color: white;
        }

        /* RESULT BOX */
        .approved {
            background-color: #e6f9f0;
            padding: 15px;
            border-radius: 8px;
            color: #065f46;
            font-weight: bold;
        }

        .rejected {
            background-color: #fdecea;
            padding: 15px;
            border-radius: 8px;
            color: #991b1b;
            font-weight: bold;
        }

    </style>
    """,
    unsafe_allow_html=True
)


# This line displays the app title.
st.title("Loan Eligibility Prediction")

# This line displays a short description.
st.write("Enter applicant details to check loan approval status.")


# This creates two columns for layout.
col1, col2 = st.columns(2)


# LEFT SIDE INPUT FORM
with col1:

    # This opens a styled container.
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # This creates input fields for user data.
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["No", "Yes"])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    applicant_income = st.number_input("Applicant Income", min_value=0.0, value=5000.0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0, value=0.0)

    loan_amount = st.number_input("Loan Amount", min_value=0.0, value=128.0)
    loan_term = st.number_input("Loan Term (months)", min_value=0.0, value=360.0)

    credit_history = st.selectbox("Credit History", [1.0, 0.0])

    # This creates the prediction button.
    predict_btn = st.button("Predict Loan Status")

    # This closes the styled container.
    st.markdown('</div>', unsafe_allow_html=True)


# RIGHT SIDE RESULT PANEL
with col2:

    # This opens a styled container.
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # This shows summary info.
    st.subheader("Application Summary")

    total_income = applicant_income + coapplicant_income

    st.write(f"Total Income: {total_income}")
    st.write(f"Loan Amount: {loan_amount}")
    st.write(f"Loan Term: {loan_term} months")

    # This checks if prediction button was clicked.
    if predict_btn:

        # This creates a dictionary of user inputs.
        user_data = {
            "Gender": gender,
            "Married": married,
            "Dependents": dependents,
            "Education": education,
            "Self_Employed": self_employed,
            "ApplicantIncome": applicant_income,
            "CoapplicantIncome": coapplicant_income,
            "LoanAmount": loan_amount,
            "Loan_Amount_Term": loan_term,
            "Credit_History": credit_history,
            "Property_Area": property_area,
        }

        try:
            # This calls the prediction function.
            result = predict_loan_status(user_data)

            # This displays result based on prediction.
            if result == "Approved":
                st.markdown(
                    '<div class="approved">Loan Approved</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    '<div class="rejected">Loan Not Approved</div>',
                    unsafe_allow_html=True
                )

        except Exception as e:
            # This shows error if prediction fails.
            st.error(f"Error: {e}")

    # This closes the styled container.
    st.markdown('</div>', unsafe_allow_html=True)