import streamlit as st
from PIL import Image
from predict_page import show_predict_page

def Predict():
    
    image = Image.open('img/Logo1.png')
    st.image(image, caption='')
    # st.markdown(
    #     f'<div class="myDiv">'
    #     f'<h2>This is a heading in a div element</h2>'
    #     f'<p>This is some text in a div element.</p>'
    #     f'</div>',
    #     unsafe_allow_html=True
    # )
    st.title("Welcome to MindMoodMeter,")
    name = st.text_input("Enter your name:")
    st.button("Go next")
    
    if name != "" :
        show_predict_page(name)  
     
if __name__ == "__main__":
    Predict()


