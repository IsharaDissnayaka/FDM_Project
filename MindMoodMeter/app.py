import streamlit as st
from main_page import Predict
from aboutus import aboutus
from Stress_management_tips_page import Stress_management_tips
from explore_page import Explore


page = st.sidebar.selectbox("Menu", ("Stress Assessment","Stress factors","Stress management tips","About Us"))

if page == "Stress Assessment":
    Predict()
elif page == "Stress factors":
    Explore()
elif page == "About Us":
    aboutus()
else:
    Stress_management_tips()
