import streamlit as st
from PIL import Image


def aboutus():
    image = Image.open('img/logo2.png')
    st.image(image,  caption='')

    st.markdown(
        f'<div style="text-align: center;"><h1>About Us</h1></div>',
        unsafe_allow_html=True
    )
    
    st.markdown(
        """<div style="text-align: center;"><p>We're here to help you navigate university life with less stress and more well-being.
        
<b>Our Mission:</b>

Our mission is simple: to enhance your mental well-being throughout your university journey. Stress can affect everything from your health to your relationships. We're here to help you understand, manage, and reduce stress so you can thrive.

<b>What We Offer:</b>

1.	Stress Assessment: Our tool evaluates your stress levels, offering insights into what might be causing your stress.

2.	Stress Management Tips: We provide expert tips to help you manage stress effectively, from mindfulness techniques to lifestyle adjustments.

<b>Who We Are:</b>

We're a team of psychologists, tech experts, and mental health advocates working together to support you.

<b>Privacy and Security:</b>

Your privacy is a priority. We've implemented strong security measures to protect your data and adhere to data protection regulations.

<b>Join Us on This Journey:</b>

Thank you for choosing [Your App Name] to make your university life less stressful and more fulfilling. Got questions or feedback? Reach out anytime. Your well-being is our top concern. Together, we'll navigate university life and help you make the most of it.
</p></div>""",
        unsafe_allow_html=True
    )                         