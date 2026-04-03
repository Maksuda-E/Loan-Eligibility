#  imports Streamlit for building the user interface.
import streamlit as st

#  imports the prediction function from the project.
from src.predict import predict_loan_status

#  sets the page configuration for the Streamlit app.
st.set_page_config(
    page_title="Loan Eligibility Prediction",
    page_icon="📄",
    layout="wide",
)

#  injects custom CSS to keep the layout neat and professional.
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
        }
        .main-title {
            font-size: 2.2rem;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 0.2rem;
        }
        .sub-title {
            font-size: 1rem;
            color: #4b5563;
            margin-bottom: 1.5rem;
        }
        .card {
            background-color: white;
            padding: 1.25rem;
            border-radius: 16px;
            box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);
            border: 1px solid #e5e7eb;
        }
        .result-approved {
            background-color: #ecfdf5;
            color: #065f46;
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid #a7f3d0;
            font-weight: 600;
        }
        .result-rejected {
            background-color: #fef2f2;
            color: #991b1b;
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid #fecaca;
            font-weight: 600;
        }
        .mini-note {
            color: #6b7280;
            font-size: 0.92rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

#  displays the page title.
st.markdown('<div class="main-title">Loan Eligibility Prediction</div>', unsafe_allow_html=True)

#  displays the short description below the title.
st.markdown(
    '<div class="sub-title">Enter applicant details and estimate whether the loan is likely to be approved.</div>',
    unsafe_allow_html=True,
)

#  creates two main columns for the form and the summary panel.
left_col, right_col = st.columns([2.2, 1], gap="large")

# This block builds the main input form column.
with left_col:
    #  opens a styled card container.
    st.markdown('<div class="card">', unsafe_allow_html=True)

    #  adds a section heading.
    st.subheader("Applicant Information")

    #  creates the first row of form fields.
    col1, col2, col3 = st.columns(3)

    # This block creates the gender input.
    with col1:
        #  creates a dropdown for gender.
        gender = st.selectbox("Gender", ["Male", "Female"])

    # This block creates the married input.
    with col2:
        #  creates a dropdown for marital status.
        married = st.selectbox("Married", ["Yes", "No"])

    # This block creates the dependents input.
    with col3:
        #  creates a dropdown for number of dependents.
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])

    #  creates the second row of form fields.
    col4, col5, col6 = st.columns(3)

    # This block creates the education input.
    with col4:
        #  creates a dropdown for education level.
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])

    # This block creates the self employment input.
    with col5:
        #  creates a dropdown for self employment status.
        self_employed = st.selectbox("Self Employed", ["No", "Yes"])

    # This block creates the property area input.
    with col6:
        #  creates a dropdown for property area.
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    #  creates the third row of numeric fields.
    col7, col8 = st.columns(2)

    # This block creates the applicant income input.
    with col7:
        #  creates a numeric input for applicant income.
        applicant_income = st.number_input(
            "Applicant Income",
            min_value=0.0,
            value=5000.0,
            step=100.0,
        )

    # This block creates the coapplicant income input.
    with col8:
        #  creates a numeric input for coapplicant income.
        coapplicant_income = st.number_input(
            "Coapplicant Income",
            min_value=0.0,
            value=0.0,
            step=100.0,
        )

    #  creates the fourth row of numeric fields.
    col9, col10, col11 = st.columns(3)

    # This block creates the loan amount input.
    with col9:
        #  creates a numeric input for loan amount.
        loan_amount = st.number_input(
            "Loan Amount",
            min_value=0.0,
            value=128.0,
            step=1.0,
            help="Loan amount requested in thousands of dollars based on the original dataset meaning.",
        )

    # This block creates the loan term input.
    with col10:
        #  creates a numeric input for loan amount term.
        loan_amount_term = st.number_input(
            "Loan Amount Term",
            min_value=0.0,
            value=360.0,
            step=12.0,
            help="Loan repayment term in months.",
        )

    # This block creates the credit history input.
    with col11:
        #  creates a dropdown for credit history.
        credit_history = st.selectbox(
            "Credit History",
            [1.0, 0.0],
            format_func=lambda value: "Good History (1.0)" if value == 1.0 else "Poor or No History (0.0)",
        )

    #  adds a small space before the button.
    st.write("")

    #  creates the prediction button.
    predict_button = st.button("Predict Loan Status", use_container_width=True)

    #  closes the styled card container.
    st.markdown('</div>', unsafe_allow_html=True)

# This block builds the summary and result panel.
with right_col:
    #  opens a styled card container.
    st.markdown('<div class="card">', unsafe_allow_html=True)

    #  adds the summary heading.
    st.subheader("Application Summary")

    #  calculates total monthly income.
    total_income = applicant_income + coapplicant_income

    #  shows the total monthly income.
    st.metric("Total Monthly Income", f"{total_income:,.0f}")

    #  shows the requested loan amount.
    st.metric("Requested Loan Amount", f"{loan_amount:,.0f}")

    #  shows the repayment term.
    st.metric("Repayment Term", f"{loan_amount_term:,.0f} months")

    #  displays a short model note.
    st.markdown(
        '<div class="mini-note">The prediction uses the same cleaned feature flow as the training pipeline.</div>',
        unsafe_allow_html=True,
    )

    #  closes the styled card container.
    st.markdown('</div>', unsafe_allow_html=True)

    #  adds spacing before the result area.
    st.write("")

    #  checks whether a prediction exists in the session state.
    if "loan_result" in st.session_state:
        #  reads the saved prediction result.
        saved_result = st.session_state["loan_result"]

        #  checks whether the saved result is approved.
        if saved_result == "Approved":
            #  displays the positive result message.
            st.markdown(
                '<div class="result-approved">Prediction Result: Approved</div>',
                unsafe_allow_html=True,
            )
        else:
            #  displays the negative result message.
            st.markdown(
                '<div class="result-rejected">Prediction Result: Not Approved</div>',
                unsafe_allow_html=True,
            )

#  checks whether the user clicked the prediction button.
if predict_button:
    #  builds the input dictionary using the form values.
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
        "Property_Area": property_area,
    }

    #  starts safe execution for prediction.
    try:
        #  gets the prediction result from the model pipeline.
        result = predict_loan_status(user_input)

        #  stores the prediction in session state.
        st.session_state["loan_result"] = result

        #  reruns the app so the result appears immediately.
        st.rerun()

    # This block handles any prediction error.
    except Exception as exc:
        #  shows a readable error message in the app.
        st.error(f"Prediction failed: {exc}")