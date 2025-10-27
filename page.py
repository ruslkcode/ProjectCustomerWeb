import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("best_knn_pipeline.joblib")


st.set_page_config(page_title="Customer Loyalty Predictor", page_icon="📊")


st.title("Welcome to the Streamlit App")
st.subheader("where we predict customer loyalty")
st.markdown("---")


with st.form("user_input_form"):
    st.header("Personal Information")
    
    age = st.number_input("Age:", min_value=18, max_value=100, value=30, step=1)
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
    
    
    having_children_flg = st.radio("Having Children:", 
                                 options=[1, 0], 
                                 format_func=lambda x: "Yes" if x == 1 else "No")
    
    
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


    is_client = st.radio("Is Client:", 
                       options=[1, 0], 
                       format_func=lambda x: "Yes" if x == 1 else "No",
                       index=1)
    
    submit_button = st.form_submit_button(label="Predict Loyalty")
    
    
if submit_button:
    
    input_df = pd.DataFrame([{
        "age": age,
        "education": education,
        "income": income,
        "credit_amount": credit_amount,
        "credit_term": credit_term,
        "having_children_flg": having_children_flg,
        "product_type": product_type,
        "is_client": is_client
    }])
    
    categorical_cols = ['education', 'product_type', 'is_client', 'having_children_flg']
    for col in categorical_cols:
        input_df[col] = input_df[col].astype(str)
        
    numeric_cols = ['age', 'income', 'credit_amount', 'credit_term']
    for col in numeric_cols:
        input_df[col] = input_df[col].astype(float)
    
    prediction_proba = model.predict_proba(input_df)[0][1]
    prediction = "Bad Client" if prediction_proba > 0.25 else "Loyal Client"
    
    
    st.markdown(f"## Prediction Result: **{prediction}**")
