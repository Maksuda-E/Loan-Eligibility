# This line imports Streamlit for building the web application.
import streamlit as st

# This line imports the loan prediction function from the project module.
from src.predict import predict_loan_status


# This line sets the page configuration for the app.
st.set_page_config(page_title="Loan Eligibility Prediction", layout="wide")


# This block injects custom CSS for styling the application.
st.markdown(
    """
    <style>
    /* REMOVE HEADER */
    header {visibility: hidden;}

    /* REMOVE TOP SPACE */
    .block-container {
        padding-top: 1rem !important;
    }

    /* APP BACKGROUND */
    .stApp {
        background-color: white;
    }

    /* Titles */
    h1 {
        color: #166534;
        font-weight: 700;
    }

    h2, h3 {
        color: #14532d;
        font-weight: 600;
    }

    p, label {
        color: #374151;
    }

    /* Input fields */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        background-color: #f0fdf4;
        border-radius: 8px;
        border: 1px solid #4b5563;
    }

    /* Metrics */
    div[data-testid="stMetric"] {
        background: white;
        border-radius: 12px;
        padding: 16px;
        border: 1px solid #dcfce7;
    }

    /* Info box */
    div[data-testid="stInfo"] {
        background: #dcfce7;
        color: #166534;
        border-radius: 10px;
        border: 1px solid #86efac;
    }

    /* Normal button */
    div.stButton > button {
        background-color: #16a34a;
        color: white;
        border-radius: 8px;
        padding: 10px;
        font-weight: 600;
        border: none;
        width: 100%;
        height: 46px;
    }

    div.stButton > button:hover {
        background-color: #15803d;
        color: white;
    }

    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: #dcfce7;
    }

    /* Result boxes */
    .approved-box {
        background: #dcfce7;
        color: #166534;
        border: 1px solid #86efac;
        border-radius: 12px;
        padding: 16px;
        font-weight: 700;
        margin-top: 16px;
    }

    .rejected-box {
        background: #fee2e2;
        color: #991b1b;
        border: 1px solid #fca5a5;
        border-radius: 12px;
        padding: 16px;
        font-weight: 700;
        margin-top: 16px;
    }

    /* White card using Streamlit container wrapper */
    .custom-card {
        background: white;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #dcfce7;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# This line displays the styled hero header section.
st.markdown(
    """
    <div style="
        background: #166534;
        padding: 32px;
        border-radius: 20px;
        margin-bottom: 24px;
        box-shadow: 0 18px 36px rgba(22, 101, 52, 0.20);
    ">
        <h1 style="color: white; margin: 0; font-size: 2.6rem; font-weight: 800;">
            Loan Eligibility Prediction
        </h1>
        <p style="color: #dcfce7; margin-top: 12px; font-size: 1.1rem;">
            Predict loan approval using the trained machine learning model.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# This line creates the main two-column dashboard layout.
left_col, right_col = st.columns([3, 1])


# This block builds the left section of the page.
with left_col:
    # This line displays the section title.
    st.subheader("Enter Applicant Details")

    # This line creates two columns for form input arrangement.
    form_col1, form_col2 = st.columns(2)

    # This block contains the first group of user inputs.
    with form_col1:
        # This line creates a dropdown for gender.
        gender = st.selectbox("Gender", ["Male", "Female"])

        # This line creates a dropdown for marital status.
        married = st.selectbox("Married", ["Yes", "No"])

        # This line creates a dropdown for number of dependents.
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])

        # This line creates a dropdown for education level.
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])

        # This line creates a dropdown for self-employment status.
        self_employed = st.selectbox("Self Employed", ["No", "Yes"])

    # This block contains the second group of user inputs.
    with form_col2:
        # This line creates a dropdown for property area.
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

        # This line creates a numeric input for applicant income.
        applicant_income = st.number_input(
            "Applicant Income",
            min_value=0.0,
            value=5000.0,
            step=100.0,
        )

        # This line creates a numeric input for coapplicant income.
        coapplicant_income = st.number_input(
            "Coapplicant Income",
            min_value=0.0,
            value=0.0,
            step=100.0,
        )

        # This line creates a numeric input for loan amount.
        loan_amount = st.number_input(
            "Loan Amount",
            min_value=0.0,
            value=128.0,
            step=1.0,
        )

        # This line creates a numeric input for loan term.
        loan_term = st.number_input(
            "Loan Term (months)",
            min_value=0.0,
            value=360.0,
            step=12.0,
        )

        # This line creates a dropdown for credit history.
        credit_history = st.selectbox("Credit History", [1.0, 0.0])

    # This line creates a full-width prediction button.
    predict_btn = st.button("Predict Loan Status")


# This block builds the right section of the page.
with right_col:
    # This line displays the section title.
    st.subheader("Model Information")

    # This line displays model information in an info box.
    st.info("Model Used: Logistic Regression")

    # This line displays the model accuracy.
    st.write("Accuracy: ~80%")

    # This line displays a short note about the training pipeline.
    st.write("Based on cleaned dataset and preprocessing pipeline")

    # This line shows a few useful summary metrics.
    st.metric("Applicant Income", f"{applicant_income:,.0f}")
    st.metric("Loan Amount", f"{loan_amount:,.0f}")
    st.metric("Loan Term", f"{loan_term:,.0f} months")


# This block runs when the user clicks the prediction button.
if predict_btn:
    # This line prepares the user input dictionary for the prediction function.
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

    # This block safely handles prediction.
    try:
        # This line gets the loan eligibility result from the trained model.
        result = predict_loan_status(user_data)

        # This line adds a visual divider before showing the result.
        st.markdown("<hr>", unsafe_allow_html=True)

        # This line shows a heading for the result section.
        st.subheader("Prediction Result")

        # This block displays the approved message.
        if result == "Approved":
            st.markdown(
                '<div class="approved-box">Loan Approved</div>',
                unsafe_allow_html=True,
            )

        # This block displays the rejected message.
        else:
            st.markdown(
                '<div class="rejected-box">Loan Not Approved</div>',
                unsafe_allow_html=True,
            )

    # This block displays any error that occurs during prediction.
    except Exception as e:
        st.error(f"Error: {e}")