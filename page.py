import streamlit as st
import data_manipulations as dm
import sql_queries as sqr


st.set_page_config(page_title="Customer Loyalty Predictor", page_icon="📊")


st.title("Welcome to the Streamlit App")
st.subheader("where we predict customer loyalty")
st.markdown("---")


with st.form("user_input_form"):
    st.header("Personal Information")
    
    age = st.number_input("Age:", min_value=18, max_value=100, value=30, step=1)
    sex = st.radio("Sex:", options=["male", "female"], index=0)
    education = st.selectbox("Education:", 
                           options=["Higher education", "Secondary special education","Secondary education", "Other"])
    
    st.header("Financial Information")
    
    income = st.number_input("Annual Income (USD):", 
                           min_value=1000, 
                           max_value=500000, 
                           value=50000, 
                           step=1000)
    
    credit_amount = st.number_input("Credit Amount:", 
                                  min_value=1000, 
                                  max_value=500000, 
                                  value=5000, 
                                  step=1000)
    
    credit_term = st.number_input("Credit Term (months):", 
                                min_value=1, 
                                max_value=60, 
                                value=12, 
                                step=1)
    
    st.header("Family & Contact Information")
    
    family_status = st.selectbox("Family Status:", 
                               options=["Married","Unmarried", "Another"])
    
    having_children_flg = st.radio("Having Children:", 
                                 options=[1, 0], 
                                 format_func=lambda x: "Yes" if x == 1 else "No")
    
    region = st.number_input("Region:", 
                           min_value=1, 
                           max_value=10, 
                           value=2, 
                           step=1)
    
    phone_operator = st.number_input("Phone Operator:", 
                                   min_value=1, 
                                   max_value=5, 
                                   value=1, 
                                   step=1)
    
    st.header("Product & Behavioral Information")
    
    product_type = st.selectbox("Product Type:", 
                              options=["Household appliances",
                                       "Cell phones",
                                       "Computers",
                                       "Furniture",
                                       "Tourism",
                                       "Construction Materials",
                                       "Jewelry",
                                       "Windows & Doors",
                                       "Clothing",
                                       "Auto",
                                       "Audio & Video",
                                       "Fitness",
                                       "Training",
                                       "Cosmetics and beauty services",
                                       "Music",
                                       "Sporting goods",
                                       "Fishing and hunting supplies",
                                       "Repair Services",
                                       "Boats",
                                       "Childrens' goods",
                                       "Other products"])

    
    month = st.number_input("Month:", 
                          min_value=1, 
                          max_value=12, 
                          value=3, 
                          step=1)
    
    is_client = st.radio("Is Client:", 
                       options=[1, 0], 
                       format_func=lambda x: "Yes" if x == 1 else "No",
                       index=1)
    
    submit_button = st.form_submit_button(label="Predict Loyalty")
    
    
