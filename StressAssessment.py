import streamlit as st
from PIL import Image

def Stress_Assessment():
    image = Image.open('img/logo2.png')
    st.image(image,  caption='')

    st.markdown(
        f'<div style="text-align:Center;"><h1>Stress Assessment</h1></div>',
        unsafe_allow_html=True
    )
    
    st.markdown(
        """<div style="text-align:Left;"><p>Please take a moment to complete the following questionnaire. Your responses will be kept confidential, and the information you provide will be used solely for the purpose of assessing your stress levels. Answer honestly to receive a more accurate prediction.
[Stress Assessment Form]

1.	Age: How old are you? [Input Box]

2.	Course: What is your current course of study? [Input Box]

3.	Gender: Please specify your gender. [Dropdown: Male, Female, Other]

4.	CGPA: What is your current Cumulative Grade Point Average (CGPA)? [Input Box]

5.	Depression Score: On a scale of 0 to 10, how would you rate your current level of depression? (0 = Not at all depressed, 10 = Extremely depressed) [Slider]

6.	Anxiety Score: On a scale of 0 to 10, how would you rate your current level of anxiety? (0 = Not at all anxious, 10 = Extremely anxious) [Slider]

7.	Sleep Quality: How would you rate your sleep quality? (Poor, Fair, Good, Excellent) [Dropdown]

8.	Physical Activity: How often do you engage in physical activity per week? [Dropdown: 0, 1-2, 3-4, 5+]

9.	Diet Quality: How would you describe your diet? (Healthy, Average, Unhealthy) [Dropdown]

10.	Social Support: Do you have a support system to talk to about stress? (Yes/No) [Radio Buttons]

11.	Relationship Status: Please specify your current relationship status. [Input Box]

12.	Substance Use: Do you engage in substance use? (Yes/No) [Radio Buttons]

13.	Counseling Service Use: Have you ever used counseling services? (Yes/No) [Radio Buttons]

14.	Family History: Is there a family history of stress-related issues? (Yes/No) [Radio Buttons]

15.	Chronic Illness: Do you have a chronic illness or health condition? (Yes/No) [Radio Buttons]

16.	Financial Stress: Are you currently experiencing financial stress? (Yes/No) [Radio Buttons]

17.	Extracurricular Involvement: Are you involved in extracurricular activities? (Yes/No) [Radio Buttons]

18.	Semester Credit Load: How many credit hours are you currently taking this semester? [Input Box]

19.	Residence Type: What type of residence do you live in? [Input Box]
Submit Button
1
----Predicted Stress Level----
Based on your responses, we have calculated your predicted stress level. Remember, this prediction is an estimate and not a substitute for professional advice. Your well-being is important, and this assessment is designed to provide you with insights into your stress levels.

Recommendations:
We also provide personalized recommendations to help you manage and reduce your stress. Please consider these suggestions as a starting point on your journey to a more stress-free life.</p></div>""",
        unsafe_allow_html=True
    )