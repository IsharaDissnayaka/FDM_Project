import streamlit as st
from PIL import Image

def Stress_management_tips():
    image = Image.open('img/logo2.png')
    st.image(image,  caption='')

    st.markdown(
        f'<div style="text-align: center;"><h1>Unlock the Secrets to Stress-Free Living</h1></div>',
        unsafe_allow_html=True
    )
    video_url_a = "https://www.youtube.com/watch?v=64ZU2UCQdmQ"
    video_url_b = "https://www.youtube.com/watch?v=odADwWzHR24"
    video_url_c = "https://www.youtube.com/watch?v=sTANio_2E0Q"
    video_url_d = "https://www.youtube.com/watch?v=iONDebHX9qk"
    video_url_e = "https://www.youtube.com/watch?v=pexOIlhT0v0"
    video_url_f = "https://www.youtube.com/watch?v=nysjq8VIwI8"
    

    st.markdown(
        """<div style="text-align:Left;"><p>Unlock the Path to Stress-Free University Life
       In today's fast-paced academic world, stress often becomes an inevitable companion on your student journey. But the good news is that managing it effectively can make all the difference in your life. Within our app, you'll discover a treasure trove of stress management tips and techniques specially curated for university students to help you navigate the complexities of academic life and find peace within.
    </p></div>""",
        unsafe_allow_html=True
    )
    
    st.subheader("1. Mindfulness Meditation: Cultivate Inner Balance")
    st.video(video_url_a)

    st.subheader("2. Breathing Techniques: Harness the Power of Breath")
    st.video(video_url_b)

    st.subheader("3. Stress-Relief Workouts: Fuel Your Body and Mind")
    st.video(video_url_c)

    st.subheader("4. Time Management Strategies: Mastering Your Schedule")
    st.video(video_url_d)

    st.subheader("5. Healthy Eating Habits: Nourish Your Mind and Body")
    st.video(video_url_e)

    st.subheader("6. Sleep Optimization: Recharge for Academic Success")
    st.video(video_url_f)

    st.markdown(
           """<div style="text-align:Left;"><p> Whether you're grappling with chronic academic stress or simply aiming to enhance your daily well-being during your university journey, our stress management tips are here to serve as your compass. Dive in, explore, and embark on a journey to a more relaxed, focused, and fulfilled university life. Your academic success and well-being are our priorities.
</p></div>""",
        unsafe_allow_html=True
    )