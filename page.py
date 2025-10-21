import streamlit as st
import data_manipulations as dm
import sql_queries as sqr

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://www.president.gov.ua/storage/j-image-storage/26/99/93/a9a3ae3a53660b2fa48bd1c22457429d_1661239081_extra_large.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
    }

    [data-testid="stToolbar"] {
        right: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)
def show_image():
    st.image("https://substackcdn.com/image/fetch/$s_!qXa6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb9540fa-b3b5-4790-9f8b-ae50925b6915_1920x1080.jpeg")


st.image("https://www.utwente.nl/logo-stacked.png")
st.image("https://www.designyourway.net/blog/wp-content/uploads/2019/11/Mercedes-Benz-logo-cover-1280x720-1.jpg")
st.title("Welcome to the Streamlit App where we predict customer loyalty")
with st.form("user_input_form"):
    age = st.number_input("Enter Age:", min_value=18, max_value=100, value=30)
    income = st.number_input("Enter Annual Income (in USD):", min_value=1000, max_value=1000000, value=50000)
    credit_amount = st.number_input("Enter your Credit Amount:", min_value=1000, max_value=500000, value=5000)
    sex = st.radio("Select Gender:", options=["Male", "Female"], index=0)
    fam_stats = st.selectbox("Select Family Status:", options=["Married", "Another"], index=0)
    spending_score = st.number_input("Enter Spending Score (1-100):", min_value=1, max_value=100, value=50)
    submit_button = st.form_submit_button(label="Predict Loyalty", on_click = show_image)
    
    

