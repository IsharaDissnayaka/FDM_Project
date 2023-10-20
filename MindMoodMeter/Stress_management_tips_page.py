import streamlit as st
from PIL import Image

def Stress_management_tips():
    image = Image.open('img/logo2.png')
    st.image(image,  caption='')

    st.markdown(
        f'<div style="text-align: center;"><h1>Unlock the Secrets to Stress-Free Living</h1></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        """<div style="text-align:Left;"><p>Unlock the Path to Stress-Free University Life
In today's fast-paced academic world, stress often becomes an inevitable companion on your student journey. But the good news is that managing it effectively can make all the difference in your life. Within our app, you'll discover a treasure trove of stress management tips and techniques specially curated for university students to help you navigate the complexities of academic life and find peace within.

1. Mindfulness Meditation: Cultivate Inner Balance
•	YouTube - Guided Mindfulness Meditation
•	Calm - Meditation and Sleep Stories
2. Breathing Techniques: Harness the Power of Breath
•	YouTube - Deep Breathing Exercise for Stress Relief
•	Verywell Mind - Relaxation Techniques
3. Stress-Relief Workouts: Fuel Your Body and Mind
•	YouTube - Yoga for Stress Relief
•	Fitness Blender - Free Workouts
4. Time Management Strategies: Mastering Your Schedule
•	YouTube - Time Management Techniques
•	Mind Tools - Time Management Skills
5. Healthy Eating Habits: Nourish Your Mind and Body
•	YouTube - Healthy Eating Tips for Students
•	ChooseMyPlate - Healthy Eating on a Budget
6. Sleep Optimization: Recharge for Academic Success
•	YouTube - Tips for a Better Night's Sleep
•	National Sleep Foundation - Healthy Sleep Tips
7. Journaling for Emotional Release: Find Clarity in Words
•	YouTube - Journaling for Stress Relief
•	Psych Central - The Health Benefits of Journaling
8. Lifestyle Changes: Crafting a Resilient Lifestyle
•	YouTube - Creating a Stress-Resistant Lifestyle
•	American Psychological Association - Stress Management
9. Connection and Support: Building a Strong Network
•	YouTube - Building Supportive Relationships
•	HelpGuide - How to Find and Build Lasting Friendships
10. Self-Care Rituals: Embrace Well-Deserved Moments
•	YouTube - Self-Care Ideas for College Students
•	Psychology Today - The Importance of Self-Care

Whether you're grappling with chronic academic stress or simply aiming to enhance your daily well-being during your university journey, our stress management tips are here to serve as your compass. Dive in, explore, and embark on a journey to a more relaxed, focused, and fulfilled university life. Your academic success and well-being are our priorities.
</p></div>""",
        unsafe_allow_html=True
    )