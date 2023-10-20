
from itertools import count
from sklearn.feature_selection import mutual_info_classif
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import mutual_info_classif


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


def Explore():
    # Load the dataset
    data = pd.read_csv("student_mental_health_1.csv")
    # ... Your existing code for data preprocessing, model training, and evaluation ...

    # Create a Streamlit app
    st.title("Machine Learning Model Evaluation")

    # Calculate summary statistics for your data
    summary_statistics = {
        "Mean Age": sum(data['Age']) / len(data['Age']),
        # "CGPA": sum(data['CGPA']) / len(data['CGPA']),
        "Mean Semester Credit Load": sum(data['Semester_Credit_Load']) / len(data['Semester_Credit_Load']),
        # Add other statistics as needed
    }

    # Display the calculated summary statistics
    st.write("Summary Statistics:")
    st.write(summary_statistics)

    # Display a bar chart of Stress Levels
    st.subheader("Stress Level Distribution.")
    fig, ax = plt.subplots()
    ax.hist(data['Age'], bins=10, color='#333333', alpha=0.7, edgecolor='black')
    ax.set_xlabel("Age")  # Set the label for the x-axis
    ax.set_ylabel("Count")  # Set the label for the y-axis
    st.pyplot(fig)

    # Display a correlation heatmap
    st.subheader("Correlation Heatmap.")
    correlation_matrix = data.corr()
    fig, ax = plt.subplots()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)
   
   

    # # Plot a confusion matrix
    # st.subheader("Confusion Matrix")
    # cm = confusion_matrix(y_test, y_pred)
    # classes = unique_labels(y_test, y_pred)
    # plt.figure(figsize=(6, 6))
    # sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=classes, yticklabels=classes)
    # plt.xlabel('Predicted')
    # plt.ylabel('Actual')
    # st.pyplot()

    # # Display model evaluation metrics
    # st.subheader("Model Evaluation")
    # st.write("Model Accuracy:", accuracy)
    # st.write("Best Hyperparameters:", best_params)
    # st.write("Classification Report:\n", report)
