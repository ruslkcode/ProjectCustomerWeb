import streamlit as st
import data_manipulations as dm
import sql_queries as sqr

st.title("Welcome to the Streamlit App where we predict customer loyalty")
with st.form("user_input_form"):
    age = st.number_input("Enter Age:", min_value=18, max_value=100, value=30)
    income = st.number_input("Enter Annual Income (in USD):", min_value=1000, max_value=1000000, value=50000)
    credit_amount = st.number_input("Enter your Credit Amount:", min_value=1000, max_value=500000, value=5000)
    sex = st.radio("Select Gender:", options=["Male", "Female"], index=0)
    fam_stats = st.selectbox("Select Family Status:", options=["Married", "Another"], index=0)
    spending_score = st.number_input("Enter Spending Score (1-100):", min_value=1, max_value=100, value=50)
    submit_button = st.form_submit_button(label="Predict Loyalty")
    
    

