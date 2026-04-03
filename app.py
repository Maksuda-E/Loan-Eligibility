#  imports streamlit for the web app
import streamlit as st

#  imports the prediction function from your project
from src.predict import predict_loan_status

#  sets the page configuration
st.set_page_config(
    page_title="Loan Eligibility Prediction",
    layout="wide"
)

#  adds custom CSS styling for the app design
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8fafc, #eff6ff, #f5f3ff);
    }

    .main-title {
        font-size: 2.7rem;
        font-weight: 800;
        text-align: center;
        color: #1e1b4b;
        margin-bottom: 0.2rem;
    }

    .sub-title {
        font-size: 1.05rem;
        text-align: center;
        color: #475569;
        margin-bottom: 2rem;
    }

    .glass-box {
        background: rgba(255, 255, 255, 0.72);
        border: 1px solid rgba(148, 163, 184, 0.22);
        backdrop-filter: blur(12px);
        border-radius: 22px;
        padding: 24px;
        box-shadow: 0 12px 28px rgba(15, 23, 42, 0.08);
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #312e81;
        margin-bottom: 1rem;
    }

    .overview-card {
        background: linear-gradient(135deg, #0f766e, #2563eb);
        color: white;
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 12px 28px rgba(37, 99, 235, 0.22);
        margin-bottom: 1rem;
    }

    .overview-title {
        font-size: 1.35rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }

    .overview-text {
        font-size: 1rem;
        line-height: 1.8;
        opacity: 0.97;
    }

    .approved-card {
        background: linear-gradient(135deg, #059669, #10b981);
        color: white;
        border-radius: 18px;
        padding: 20px;
        margin-top: 1rem;
        box-shadow: 0 10px 24px rgba(16, 185, 129, 0.22);
    }

    .rejected-card {
        background: linear-gradient(135deg, #dc2626, #f97316);
        color: white;
        border-radius: 18px;
        padding: 20px;
        margin-top: 1rem;
        box-shadow: 0 10px 24px rgba(249, 115, 22, 0.22);
    }

    .result-title {
        font-size: 0.95rem;
        margin-bottom: 0.45rem;
        opacity: 0.95;
    }

    .result-value {
        font-size: 1.7rem;
        font-weight: 800;
        margin-bottom: 0.35rem;
    }

    .result-text {
        font-size: 1rem;
        opacity: 0.96;
    }

    div.stButton > button {
        width: 100%;
        height: 50px;
        border: none;
        border-radius: 14px;
        background: linear-gradient(90deg, #7c3aed, #2563eb);
        color: white;
        font-size: 1rem;
        font-weight: 700;
        box-shadow: 0 10px 22px rgba(124, 58, 237, 0.22);
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #6d28d9, #1d4ed8);
    }
    </style>
    """,
    unsafe_allow_html=True
)

#  displays the app title
st.markdown(
    '<div class="main-title">Loan Eligibility Prediction App</div>',
    unsafe_allow_html=True
)

#  displays the app subtitle
st.markdown(
    '<div class="sub-title">Enter applicant details to predict loan approval status</div>',
    unsafe_allow_html=True
)

#  creates a centered page layout
left_space, center_col, right_space = st.columns([0.5, 4, 0.5])

# This block contains the full app content
with center_col:

    #  creates two columns for form and side panel
    form_col, side_col = st.columns([2.2, 1], gap="large")

    # This block creates the form section
    with form_col:

        #  creates the first row of inputs
        row1_col1, row1_col2, row1_col3 = st.columns(3)

        # This block creates the gender input
        with row1_col1:
            gender = st.selectbox("Gender", ["Male", "Female"])

        # This block creates the married input
        with row1_col2:
            married = st.selectbox("Married", ["Yes", "No"])

        # This block creates the dependents input
        with row1_col3:
            dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])

        #  creates the second row of inputs
        row2_col1, row2_col2, row2_col3 = st.columns(3)

        # This block creates the education input
        with row2_col1:
            education = st.selectbox("Education", ["Graduate", "Not Graduate"])

        # This block creates the self employed input
        with row2_col2:
            self_employed = st.selectbox("Self Employed", ["Yes", "No"])

        # This block creates the property area input
        with row2_col3:
            property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

        #  creates the third row of numeric inputs
        row3_col1, row3_col2 = st.columns(2)

        # This block creates the applicant income input
        with row3_col1:
            applicant_income = st.number_input(
                "Applicant Income",
                min_value=0.0,
                value=5000.0
            )

        # This block creates the coapplicant income input
        with row3_col2:
            coapplicant_income = st.number_input(
                "Coapplicant Income",
                min_value=0.0,
                value=0.0
            )

        #  creates the fourth row of numeric inputs
        row4_col1, row4_col2, row4_col3 = st.columns(3)

        # This block creates the loan amount input
        with row4_col1:
            loan_amount = st.number_input(
                "Loan Amount",
                min_value=0.0,
                value=120.0
            )

        # This block creates the loan amount term input
        with row4_col2:
            loan_amount_term = st.number_input(
                "Loan Amount Term",
                min_value=0.0,
                value=360.0
            )

        # This block creates the credit history input
        with row4_col3:
            credit_history = st.selectbox("Credit History", [1.0, 0.0])

        #  adds small spacing before the button
        st.markdown("<br>", unsafe_allow_html=True)

        #  creates the prediction button
        predict_button = st.button("Predict Loan Status")

        #  closes the styled form container
        st.markdown('</div>', unsafe_allow_html=True)

    # This block creates the side panel
    with side_col:

        #  displays the overview card
        st.markdown(
            f"""
            <div class="overview-card">
                <div class="overview-title">Application Overview</div>
                <div class="overview-text">
                    This applicant profile shows a monthly income of {applicant_income:.0f} with a coapplicant contribution of {coapplicant_income:.0f}. 
                    The requested loan amount is {loan_amount:.0f} for a repayment term of {loan_amount_term:.0f} months. 
                    The application also reflects {dependents} dependents, {education.lower()} education status, 
                    self employment marked as {self_employed.lower()}, and a credit history value of {credit_history}. 
                    These are the same input details the trained model will use to estimate loan approval.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        #  checks whether a previous prediction result exists
        if "loan_result" in st.session_state:

            #  reads the stored result
            result = st.session_state["loan_result"]

            #  converts the result into lowercase text for checking
            result_text = str(result).strip().lower()

            #  checks if the result means approval
            if "approve" in result_text or result_text in ["1", "y", "yes", "eligible", "approved"]:

                #  displays the approved result card
                st.markdown(
                    f"""
                    <div class="approved-card">
                        <div class="result-title">Prediction Result</div>
                        <div class="result-value">{result}</div>
                        <div class="result-text">
                            The application appears eligible based on the trained model logic.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # This block handles non approved results
            else:

                #  displays the rejected result card
                st.markdown(
                    f"""
                    <div class="rejected-card">
                        <div class="result-title">Prediction Result</div>
                        <div class="result-value">{result}</div>
                        <div class="result-text">
                            The application appears risky based on the trained model logic.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    #  checks if the button was clicked
    if predict_button:

        #  creates the user input dictionary
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

        #  starts safe prediction handling
        try:
            #  gets the prediction result from the backend logic
            result = predict_loan_status(user_input)

            #  stores the prediction result in session state
            st.session_state["loan_result"] = result

            #  reruns the app so the result appears under the overview immediately
            st.rerun()

        # This block handles prediction errors
        except Exception as exc:
            st.error(f"Prediction failed: {exc}")
