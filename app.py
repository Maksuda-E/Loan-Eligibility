# This line imports streamlit for the web app
import streamlit as st

# This line imports the prediction function
from src.predict import predict_loan_status

# This line sets the page title and layout
st.set_page_config(
    page_title="Loan Eligibility Prediction",
    layout="wide"
)

# This line adds custom CSS for a new layout and color theme
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #eff6ff, #f8fafc, #eef2ff);
    }

    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        text-align: center;
        color: #1e1b4b;
        margin-bottom: 0.3rem;
    }

    .sub-title {
        font-size: 1.05rem;
        text-align: center;
        color: #475569;
        margin-bottom: 2.2rem;
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #312e81;
        margin-bottom: 1rem;
    }

    .info-card {
        background: linear-gradient(135deg, #312e81, #2563eb);
        color: white;
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 12px 30px rgba(37, 99, 235, 0.22);
        margin-bottom: 1.5rem;
    }

    .info-card-title {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.7rem;
    }

    .info-card-text {
        font-size: 0.98rem;
        line-height: 1.6;
        opacity: 0.95;
    }

    .result-card-approved {
        background: linear-gradient(135deg, #059669, #10b981);
        color: white;
        border-radius: 18px;
        padding: 20px;
        margin-top: 1rem;
        box-shadow: 0 10px 24px rgba(16, 185, 129, 0.22);
    }

    .result-card-rejected {
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
        font-size: 1.6rem;
        font-weight: 800;
    }

    div.stButton > button {
        width: 100%;
        height: 50px;
        border: none;
        border-radius: 14px;
        background: linear-gradient(90deg, #4f46e5, #2563eb);
        color: white;
        font-size: 1rem;
        font-weight: 700;
        box-shadow: 0 10px 22px rgba(79, 70, 229, 0.22);
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #4338ca, #1d4ed8);
    }

    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.75);
        border: 1px solid rgba(191, 219, 254, 0.8);
        border-radius: 16px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# This line displays the main title
st.markdown(
    '<div class="main-title">Loan Eligibility Prediction App</div>',
    unsafe_allow_html=True
)

# This line displays the subtitle
st.markdown(
    '<div class="sub-title">Enter applicant details to predict loan approval status</div>',
    unsafe_allow_html=True
)

# This line creates three columns to center the main content
left_space, center_col, right_space = st.columns([0.6, 3, 0.6])

# This block places the full layout inside the center column
with center_col:

    # This line creates two columns for a different layout style
    form_col, side_col = st.columns([2.2, 1], gap="large")

    # This block creates the left form section
    with form_col:

        # This line shows the form section heading
        st.markdown('<div class="section-title">Applicant Details</div>', unsafe_allow_html=True)

        # This line creates the first row of inputs
        row1_col1, row1_col2, row1_col3 = st.columns(3)

        # This block creates the gender input
        with row1_col1:
            gender = st.selectbox("Gender", ["Male", "Female"])

        # This block creates the marital status input
        with row1_col2:
            married = st.selectbox("Married", ["Yes", "No"])

        # This block creates the dependents input
        with row1_col3:
            dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])

        # This line creates the second row of inputs
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

        # This line creates the third row of numeric inputs
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

        # This line creates the fourth row of numeric inputs
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

        # This line adds small space before the button
        st.markdown("<br>", unsafe_allow_html=True)

        # This line creates the prediction button
        predict_button = st.button("Predict Loan Status")

    # This block creates the right side information panel
    with side_col:

        # This line shows an information card
        st.markdown(
            """
            <div class="info-card">
                <div class="info-card-title">Quick Overview</div>
                <div class="info-card-text">
                    Fill in the applicant profile to estimate whether the loan is likely to be approved.
                    Strong income, stable credit history, and balanced loan details usually improve approval chances.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # This line shows a summary metric for applicant income
        st.metric("Applicant Income", f"{applicant_income:.0f}")

        # This line shows a summary metric for loan amount
        st.metric("Loan Amount", f"{loan_amount:.0f}")

        # This line shows a summary metric for loan term
        st.metric("Loan Term", f"{loan_amount_term:.0f}")

    # This line checks whether the prediction button has been clicked
    if predict_button:

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

            # This line converts the result to text for checking approval status
            result_text = str(result).strip().lower()

            # This line checks if the result suggests approval
            if "approve" in result_text or result_text in ["1", "y", "yes", "eligible", "approved"]:

                # This line shows an approved result card
                st.markdown(
                    f"""
                    <div class="result-card-approved">
                        <div class="result-title">Prediction Result</div>
                        <div class="result-value">{result}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # This block handles non approved results
            else:
                # This line shows a rejected result card
                st.markdown(
                    f"""
                    <div class="result-card-rejected">
                        <div class="result-title">Prediction Result</div>
                        <div class="result-value">{result}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # This block shows error messages in the app
        except Exception as exc:
            # This line displays the error
            st.error(f"Prediction failed: {exc}")
