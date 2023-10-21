import streamlit as st
from PIL import Image
from predict_page import show_predict_page

def Predict():
    
    image = Image.open('img/Logo1.png')
    st.image(image, caption='')
    
    st.title("Welcome to MindMoodMeter,")
    st.markdown("<p style='font-size: small;'>We get it. University life can be a rollercoaster of emotions. That's where Mind Mood Meter comes in. We're your all-in-one solution for tackling those stress levels head-on.</p>", unsafe_allow_html=True)
    name = st.text_input("To start with enter your name:")
    st.button("Go next")
    
    if name != "" :
        show_predict_page(name)  
     
if __name__ == "__main__":
    Predict()


