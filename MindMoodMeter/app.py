import streamlit as st
from main_page import Predict
from aboutus import aboutus
from StressAssessment import Stress_Assessment
from Stress_management_tips_page import Stress_management_tips
from Terms_and_Privacy_page import Terms_and_Privacy
from Stress_factors_page import Stress_factors
from explore_page import Explore


page = st.sidebar.selectbox("Menu", ("Predict","Explore","Stress factors","Stress Assessment","Stress management tips","About Us"))

if page == "Predict":
    print("hello")
    Predict()
elif page == "Explore":
    Explore()
elif page == "About Us":
    aboutus()
elif page == "Stress factors":
    Stress_factors()
elif page == "Stress Assessment":
    Stress_Assessment()
elif page == "Stress management tips":
    Stress_management_tips()
    
    
else:
    print("")
    #show_explore_page()