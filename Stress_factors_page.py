import streamlit as st
from PIL import Image

def Stress_factors():
    image = Image.open('img/logo2.png')
    st.image(image,  caption='')

    st.markdown(
        f'<div style="text-align: center;"><h1>Exploring What Drives Your Stress</h1></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        """<div style="text-align: Left;"><p>Welcome to our "Stress Factors" hub, a place where we break down the puzzle of what's been keeping your stress levels up. In this space, we've translated complex data into easy-to-digest visual aids, giving you a clear picture of what's affecting your stress.


Here, you'll find interactive visuals that show how different parts of your life, both academic and personal, play into your stress levels. By uncovering these links, you'll be better equipped to make decisions that boost your well-being. This user-friendly tool helps you spot stress triggers, tackle stress head-on, and work towards a calmer and more balanced you. Dive into "Stress Factors" today to seize control of your emotional well-being.
</p></div>""",
        unsafe_allow_html=True
    )
    