import streamlit as st
import pickle
import numpy as np
import pandas as pd
import time
import streamlit as st
from PIL import Image

def load_model():
    with open('steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data=load_model()




best_model = data["model"]
Age= data["Age"]
Course= data["Course"]
Gender= data["Gender"]
CGPA= data["CGPA"]
Sleep_Quality= data["Sleep_Quality"]
Physical_Activity= data["Physical_Activity"]
Diet_Quality= data["Diet_Quality"]
Social_Support= data["Social_Support"]
Relationship_Status= data["Relationship_Status"]
Substance_Use= data["Substance_Use"]
Counseling_Service_Use= data["Counseling_Service_Use"]
Family_History= data["Family_History"]
Chronic_Illness= data["Chronic_Illness"]
Extracurricular_Involvement= data["Extracurricular_Involvement"]
Semester_Credit_Load= data["Semester_Credit_Load"]
Residence_Type = data["Residence_Type"]


                                    

def show_predict_page(name):
    
    if __name__ == "__main__":
        show_predict_page("Unknown")
    from sklearn.preprocessing import LabelEncoder

    import streamlit as st
    from sklearn.preprocessing import LabelEncoder
    
    st.write("""Hi  """+name +""",   Please take a moment to complete the following questionnaire. Your responses will be kept confidential, and the information you provide will be used solely for the purpose of assessing your stress levels. Answer honestly to receive a more accurate prediction.""")
   
    #Age = st.slider("1. Your  age ", 10, 50, 10)
    options_mapping = {'Teen (below 20)':1, 'Young Adult (between 20-30)':2, 'Adult (above 30)':0}
    Age = st.radio("1.What is your age group?", ('Teen (below 20)','Young Adult (between 20-30)','Adult (above 30)'))
    Age = options_mapping[Age]
    

    #st.write("Numerical value:", Age)

    options_mapping = {'Others':5, 'Engineering':2, 'Business':0, 'Computer Science':1, 'Medical':4, 'Law':3}
    Course = st.radio("2.What is your current course of study? ", ('Engineering', 'Business', 'Computer Science', 'Medical', 'Law','Others'))
    Course = options_mapping[Course]
    #st.write("Numerical value:", Course)


    options_mapping = {'Male':1, 'Female':0}
    Gender = st.radio("3.Please specify your gender.   ", ('Male', 'Female'))
    Gender = options_mapping[Gender]
    #st.write("Numerical value:", Gender)

    
    options_mapping = {'Low (below2.7)':2, 'Medium (2.7 - 3)':3, 'High (3 - 3.5)':1,  'Excellent (above 3.5)': 0}
    CGPA = st.radio("4.What is your current Cumulative Grade Point Average(CGPA)? ", ('Low (below2.7)', 'Medium (2.7 - 3)', 'High (3 - 3.5)', 'Excellent (above 3.5)'))
    CGPA = options_mapping[CGPA]
    #st.write("Numerical value:", CGPA)
    
    #Semester_Credit_Load = st.slider("Semester Credit_Load  ", 1, 100, 1)
    options_mapping = {'Low (below15)':1, 'Medium (15 - 20)':2, 'High (20 - 25)':0}
    Semester_Credit_Load = st.radio("5.How many total credit point are their for the semester?  ", ('Low (below15)', 'Medium (15 - 20)', 'High (20 - 25)'))
    Semester_Credit_Load = options_mapping[Semester_Credit_Load]
    #st.write("Numerical value:", Semester_Credit_Load)
        
    Depression_Score = st.slider("6.On a scale of 0 to 5, rate your current level of depression. (0 = Not at all depressed, 5 = Extremely depressed)  ", 0, 5, 0)
    
    Anxiety_Score =  st.slider("7.On a scale of 0 to 5, rate your current level of anxiety. (0 = Not at all anxious, 5 = Extremely anxious)  ", 0, 5, 0)
    
    Financial_Stress = st.slider("8.On a scale of 0 to 5,  rate your current level of financial stress. (0 = Not at all, 5 = Extremely high)", 0, 5, 1)
    

    options_mapping = {'Good':1, 'Average':0, 'Poor':2}
    Sleep_Quality = st.radio("9.How would you rate your sleep quality?  ", ('Good', 'Average', 'Poor'))
    Sleep_Quality = options_mapping[Sleep_Quality]
    #st.write("Numerical value:", Sleep_Quality)

    
    options_mapping = {'Moderate':2, 'Low':1, 'High':0}
    Physical_Activity = st.radio("10.How often do you engage in physical activity per week?  ", ( 'Low','Moderate', 'High'))
    Physical_Activity = options_mapping[Physical_Activity]
    #st.write("Numerical value:", Physical_Activity)
    

    options_mapping = {'Good':1, 'Average':0, 'Poor':2}
    Diet_Quality = st.radio("11.How would you describe your diet?  ", ('Good', 'Average', 'Poor'))
    Diet_Quality = options_mapping[Diet_Quality]
    #st.write("Numerical value:", Diet_Quality)
   
 
    options_mapping = {'Moderate':2, 'Low':1, 'High':0}
    Social_Support = st.radio("12.Do you have a support system to talk to about stress? ", ( 'Low','Moderate', 'High'))
    Social_Support = options_mapping[Social_Support]
    #st.write("Numerical value:", Social_Support)

    options_mapping = {'Married':1, 'Single':2,'In a Relationship':0}
    Relationship_Status = st.radio("13.Please specify your current relationship status. ", ('Married', 'Single','In a Relationship'))
    Relationship_Status = options_mapping[Relationship_Status]
    #st.write("Numerical value:", Relationship_Status)

    options_mapping = {'Occasionally':2, 'Never':1,'Frequently':0}
    Substance_Use = st.radio("14.Do you engage in substance use?  ", ( 'Never','Occasionally', 'Frequently'))
    Substance_Use = options_mapping[Substance_Use]
    #st.write("Numerical value:", Substance_Use)


    options_mapping = {'Never':1, 'Occasionally':2,'Frequently':0}
    Counseling_Service_Use = st.radio("15.Have you ever used counseling services?  ", ('Never', 'Occasionally','Frequently'))
    Counseling_Service_Use = options_mapping[Counseling_Service_Use]
    #st.write("Numerical value:", Counseling_Service_Use)
    

    options_mapping = {'Yes':0,'No':1}
    Family_History = st.radio("16.Is there a family history of stress-related issues?  ", ('Yes','No'))
    Family_History = options_mapping[Family_History]
    #st.write("Numerical value:", Family_History)



    options_mapping = {'Yes':0,'No':1}
    Chronic_Illness = st.radio("17.Do you have a chronic illness or health condition? ", ('Yes','No'))
    Chronic_Illness = options_mapping[Chronic_Illness]
    #st.write("Numerical value:", Chronic_Illness)
    

   
    
    
    
    options_mapping = {'Moderate':2, 'Low':1, 'High':0}
    Extracurricular_Involvement = st.radio("18.Are you involved in extracurricular activities?  ",( 'Low','Moderate', 'High'))
    Extracurricular_Involvement = options_mapping[Extracurricular_Involvement]
    #st.write("Numerical value:", Extracurricular_Involvement)
    
    


    
    options_mapping = {'On-Campus':1 ,'Off-Campus':0 ,'With Family':2}
    Residence_Type = st.radio("19 .What type of residence do you live in? ", ('On-Campus' ,'Off-Campus' ,'With Family'),key="Residence_Type")
    Residence_Type = options_mapping[Residence_Type]
    #st.write("Numerical value:", Residence_Type)
    
    

    if st.button("Calculate",key="calculate"):
        X = np.array([[Age,Course,Gender,CGPA,Depression_Score,Anxiety_Score,Sleep_Quality,Physical_Activity,Diet_Quality,Social_Support,Relationship_Status,Substance_Use,Counseling_Service_Use,Family_History,Chronic_Illness,Financial_Stress,Extracurricular_Involvement,Residence_Type]])
        #X = np.array([[19, 0, 0, 3.74, 0, 3, 1, 1, 0, 2, 0, 1, 2, 0, 0, 4, 0, 15, 1]])
        #st.title(X)
        # X[:, 1] = Course.transform([X[:, 1]])
        # X[:, 2] = Gender.transform([X[:, 2]])
        # X[:, 6] = Sleep_Quality.transform([X[:, 6]])
        # X[:, 7] = Physical_Activity.transform([X[:, 7]])    
        # X[:, 8] = Diet_Quality.transform([X[:, 8]])
        # X[:, 9] = Social_Support.transform([X[:, 9]])
        # X[:, 10] = Relationship_Status.transform([X[:, 10]])
        # X[:, 11] = Substance_Use.transform([X[:, 11]])
        # X[:, 12] = Counseling_Service_Use.transform([X[:, 12]])
        # X[:, 13] = Family_History.transform([X[:, 13]])
        # X[:, 14] = Chronic_Illness.transform([X[:, 14]])
        # X[:, 16] = Extracurricular_Involvement.transform([X[:, 16]])
        # X[:, 18] = Residence_Type.transform([X[:, 18]])

       # Convert X to float
        X = X.astype(float)
       
        y_pred = best_model.predict(X)
        Score=y_pred[0]
        # st.title("1 = Low")
        # st.title("2 = nomal ")
        # st.title("3 = medium")
        # st.title("4 = high ")
        # st.title("5 = very high ")
        st.markdown(
        f'<h1>Your Stress Level is ... </h1>',
        unsafe_allow_html=True
        )
        with st.spinner('Wait for it...'):
            time.sleep(5)  
            if Score == 0:
                image = Image.open('img/lev1.png')
                st.image(image, width=100, caption='')
                st.markdown(
                """<div "><h4>Stress Level 0 (No Stress):</h4></div>
                <div "><p>Congratulations! You're currently experiencing low or no stress. Keep up the good work in maintaining a balanced and stress-free life. Remember, stress management is about staying proactive, even when stress levels are low</p></div>""",
                unsafe_allow_html=True
            )
            elif Score == 1:
                image = Image.open('img/lev2.png')
                st.image(image, width=100, caption='')
                st.markdown(
                """<div "><h4>Stress Level 1 (Low Stress):</h4></div>
                <div "><p>You're doing well with low stress levels! It's essential to continue practicing self-care and stress reduction techniques to maintain your well-being. Keep up the positive habits.</p></div>""",
                unsafe_allow_html=True
            )
            elif Score == 2:
                image = Image.open('img/lev4.png')
                st.image(image, width=100, caption='')
                st.markdown(
                """<div "><h4>Stress Level 2 (Moderate Stress):</h4></div>
                <div "><p>Moderate stress can be a part of life, but it's essential to address it to prevent it from escalating. Take some time for self-care and consider stress-reduction strategies to manage this level of stress effectively</p></div>""",
                unsafe_allow_html=True
            )
            elif Score == 3:
                image = Image.open('img/lev5.png')
                st.image(image, width=100, caption='')
                st.markdown(
                """<div "><h4>Stress Level 3 (High Stress):</h4></div>
                <div "><p>High stress levels can take a toll on your well-being. It's crucial to take immediate action to reduce stress. Consider speaking to a professional or using our stress management tools for support. Prioritize your mental health.</p></div>""",
                unsafe_allow_html=True
            )
            else:
                image = Image.open('img/lev6.png')
                st.image(image, width=100, caption='')
                st.markdown(
                """<div "><h4>Nomal</h4></div>
                <div "><p>High stress levels can take a toll on your well-being. It's crucial to take immediate action to reduce stress. Consider speaking to a professional or using our stress management tools for support. Prioritize your mental health.</p></div>""",
                unsafe_allow_html=True
            )                              
            
            

        
