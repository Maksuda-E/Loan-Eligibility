# This line imports Streamlit for UI.
import streamlit as st

# This line imports prediction function.
from src.predict import predict_loan_status


# This line sets page configuration.
st.set_page_config(page_title="Loan Eligibility", layout="wide")


# This block adds custom CSS styling.
st.markdown(
    """
    <style>

        /* HIDE STREAMLIT DEFAULT HEADER ELEMENTS */
        header {
            visibility: hidden;
            height: 0rem;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        div[data-testid="stToolbar"] {
            display: none;
        }

        div[data-testid="stDecoration"] {
            display: none;
        }

        div[data-testid="stStatusWidget"] {
            display: none;
        }

        div[data-testid="stHeader"] {
            display: none;
        }

        /* REMOVE TOP SPACE */
        .block-container {
            padding-top: 0.2rem !important;
            padding-bottom: 1rem !important;
        }

        /* PULL APP UPWARD */
        .stApp {
            background-color: #FAFAF5;
            margin-top: -3.5rem;
        }

        /* REMOVE EXTRA WRAPPER SPACING */
        section.main > div {
            padding-top: 0rem !important;
        }

        /* HEADER BANNER */
        .header-box {
            background-color: #166534;
            padding: 25px;
            border-radius: 12px;
            color: white;
            margin-bottom: 20px;
        }

        /* CARD STYLE */
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        }

        /* BUTTON STYLE */
        div.stButton > button {
            background-color: #16a34a;
            color: white;
            border-radius: 8px;
            height: 45px;
            font-size: 16px;
            font-weight: 600;
            border: none;
            width: 100%;
        }

        div.stButton > button:hover {
            background-color: #15803d;
            color: white;
        }

        /* RESULT BOX */
        .approved {
            background-color: #dcfce7;
            color: #166534;
            padding: 15px;
            border-radius: 8px;
            font-weight: bold;
        }

        .rejected {
            background-color: #fee2e2;
            color: #991b1b;
            padding: 15px;
            border-radius: 8px;
            font-weight: bold;
        }

    </style>
    """,
    unsafe_allow_html=True
)


# HEADER SECTION
st.markdown(
    """
    <div class="header-box">
        <h2>Loan Eligibility Prediction</h2>
        <p>Predict loan approval using trained machine learning model</p>
    </div>
    """,
    unsafe_allow_html=True
)


# MAIN LAYOUT
col1, col2 = st.columns([3, 1])


# LEFT SIDE FORM
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Enter Applicant Details")

    colA, colB = st.columns(2)

    with colA:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["No", "Yes"])

    with colB:
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
        applicant_income = st.number_input("Applicant Income", value=5000.0)
        coapplicant_income = st.number_input("Coapplicant Income", value=0.0)
        loan_amount = st.number_input("Loan Amount", value=128.0)
        loan_term = st.number_input("Loan Term (months)", value=360.0)
        credit_history = st.selectbox("Credit History", [1.0, 0.0])

    # BUTTON
    predict_btn = st.button("Predict Loan Status")

    st.markdown('</div>', unsafe_allow_html=True)


# RIGHT SIDE INFO PANEL
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Model Information")

    st.info("Model Used: Logistic Regression")

    st.write("Accuracy: ~80%")
    st.write("Based on cleaned dataset and preprocessing pipeline")

    st.markdown('</div>', unsafe_allow_html=True)


# PREDICTION LOGIC
if predict_btn:

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
        result = predict_loan_status(user_data)

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
        st.error(f"Error: {e}")