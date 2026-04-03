#  imports Streamlit for building the web app interface.
import streamlit as st

#  imports the prediction function from the project pipeline.
from src.predict import predict_loan_status


#  sets the page configuration for the Streamlit app.
st.set_page_config(
    page_title="Loan Eligibility",
    layout="wide",
)


# This block adds custom CSS styling to remove Streamlit spacing and improve the UI.
st.markdown(
    """
    <style>

        /* HIDE STREAMLIT DEFAULT UI */
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

        /* REMOVE EXTRA TOP SPACE */
        .block-container {
            padding-top: 0.4rem !important;
            padding-bottom: 1rem !important;
        }

        section.main > div {
            padding-top: 0rem !important;
        }

        .stApp {
            background-color: #FAFAF5;
            margin-top: -2.8rem;
        }

        /* REMOVE EMPTY GAP AFTER HEADER */
        div[data-testid="stHorizontalBlock"] {
            margin-top: 0rem !important;
            padding-top: 0rem !important;
            gap: 1rem;
        }

        div[data-testid="element-container"]:empty {
            display: none !important;
        }

        /* HEADER BANNER */
        .header-box {
            background-color: #166534;
            padding: 24px 28px;
            border-radius: 14px;
            color: white;
            margin-bottom: 1rem;
        }

        .header-title {
            font-size: 2rem;
            font-weight: 700;
            margin: 0;
        }

        .header-subtitle {
            font-size: 1rem;
            margin-top: 0.35rem;
            margin-bottom: 0;
            opacity: 0.95;
        }

        /* CARD STYLE */
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.06);
            border: 1px solid #e5e7eb;
        }

        /* BUTTON STYLE */
        div.stButton > button {
            background-color: #16a34a;
            color: white;
            border-radius: 10px;
            height: 46px;
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
            border-radius: 10px;
            font-weight: 700;
            border: 1px solid #86efac;
        }

        .rejected {
            background-color: #fee2e2;
            color: #991b1b;
            padding: 15px;
            border-radius: 10px;
            font-weight: 700;
            border: 1px solid #fca5a5;
        }

    </style>
    """,
    unsafe_allow_html=True,
)


#  creates the top green header section.
st.markdown(
    """
    <div class="header-box">
        <p class="header-title">Loan Eligibility Prediction</p>
        <p class="header-subtitle">Predict loan approval using the trained machine learning model.</p>
    </div>
    """,
    unsafe_allow_html=True,
)


#  creates a main container so the content starts immediately after the header.
main_container = st.container()


# This block places the full page content inside the main container.
with main_container:
    #  creates the two-column dashboard layout.
    col1, col2 = st.columns([3, 1])

    # This block creates the left side input form section.
    with col1:
        #  opens a styled form card.
        st.markdown('<div class="card">', unsafe_allow_html=True)

        #  shows the section title.
        st.subheader("Enter Applicant Details")

        #  creates two inner columns for arranging inputs.
        col_a, col_b = st.columns(2)

        # This block holds the first group of input fields.
        with col_a:
            #  creates the gender input.
            gender = st.selectbox("Gender", ["Male", "Female"])

            #  creates the married input.
            married = st.selectbox("Married", ["Yes", "No"])

            #  creates the dependents input.
            dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])

            #  creates the education input.
            education = st.selectbox("Education", ["Graduate", "Not Graduate"])

            #  creates the self-employed input.
            self_employed = st.selectbox("Self Employed", ["No", "Yes"])

        # This block holds the second group of input fields.
        with col_b:
            #  creates the property area input.
            property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

            #  creates the applicant income input.
            applicant_income = st.number_input(
                "Applicant Income",
                min_value=0.0,
                value=5000.0,
                step=100.0,
            )

            #  creates the coapplicant income input.
            coapplicant_income = st.number_input(
                "Coapplicant Income",
                min_value=0.0,
                value=0.0,
                step=100.0,
            )

            #  creates the loan amount input.
            loan_amount = st.number_input(
                "Loan Amount",
                min_value=0.0,
                value=128.0,
                step=1.0,
            )

            #  creates the loan term input.
            loan_term = st.number_input(
                "Loan Term (months)",
                min_value=0.0,
                value=360.0,
                step=12.0,
            )

            #  creates the credit history input.
            credit_history = st.selectbox("Credit History", [1.0, 0.0])

        #  creates the prediction button.
        predict_btn = st.button("Predict Loan Status")

        #  closes the styled form card.
        st.markdown("</div>", unsafe_allow_html=True)

    # This block creates the right side model information section.
    with col2:
        #  opens a styled information card.
        st.markdown('<div class="card">', unsafe_allow_html=True)

        #  shows the side panel title.
        st.subheader("Model Information")

        #  displays the model name.
        st.info("Model Used: Logistic Regression")

        #  displays the approximate model accuracy.
        st.write("Accuracy: ~80%")

        #  displays a short note about preprocessing.
        st.write("Based on cleaned dataset and preprocessing pipeline")

        #  closes the styled information card.
        st.markdown("</div>", unsafe_allow_html=True)


# This block runs the prediction only after the user clicks the button.
if predict_btn:
    #  creates the input dictionary expected by the prediction function.
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

    # This block handles prediction and error checking safely.
    try:
        #  gets the prediction result from the saved model.
        result = predict_loan_status(user_data)

        #  adds a small gap before the result.
        st.write("")

        # This block shows the approved result style.
        if result == "Approved":
            st.markdown(
                '<div class="approved">Loan Approved</div>',
                unsafe_allow_html=True,
            )

        # This block shows the not approved result style.
        else:
            st.markdown(
                '<div class="rejected">Loan Not Approved</div>',
                unsafe_allow_html=True,
            )

    # This block displays any error message.
    except Exception as e:
        st.error(f"Error: {e}")