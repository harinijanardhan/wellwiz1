# -*- coding: utf-8 -*-
"""WellWiz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/163TXhPgncUCKZ9s97H_Yn2njiimY_TEq
"""

import numpy as np
from sklearn.svm import SVC

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
import warnings
warnings.filterwarnings('ignore')
# %matplotlib inline

# Importing the csv file
stress_data = pd.read_csv("/content/drive/MyDrive/Chatbot/main1.csv")
stress_data

stress_data.shape

stress_data.drop(columns=['Timestamp'],inplace=True)

stress_data = stress_data.rename(columns={'How often do you feel stressed in your daily life?': 'Anxiety_level'})

stress_data = stress_data.rename(columns={'Do you find that your stress levels fluctuate throughout the day or week?': 'Stress_fluctuation'})

stress_data = stress_data.rename(columns={'How many hours a day will you sleep? (in Hours)': 'Sleeping_hours'})

stress_data = stress_data.rename(columns={'Do you exercise in a day?': 'Exercise'})

stress_data = stress_data.rename(columns={'Did you observe any change in your physical appearance?': 'Appearance_change'})

stress_data = stress_data.rename(columns={'How much work load do you have in a day?': 'Work_load_level'})

stress_data = stress_data.rename(columns={'How does stress affect your health?': 'Stress_type'})

stress_data = stress_data.rename(columns={'The situation which you feel more stressed about?': 'Situation'})

stress_data = stress_data.rename(columns={'How do you overcome it?': 'dealing_stress'})

stress_data['Stress']=stress_data['Do you personally experience stress in your daily life?']

stress_data.drop(columns=["Do you personally experience stress in your daily life?"],inplace=True)

stress_data.dtypes

stress_data

stress_data.head()

def avg(text):
  if text=='7-8':
    return int((8+7)//2)
  elif text=='6-7':
    return int((7+6)//2)
  elif text=='5-6':
    return int((5+6)//2)
  elif text=="Other":
    return int(5)

stress_data['Sleeping_hours']=stress_data['Sleeping_hours'].apply((lambda x:(avg(x))))
stress_data['Sleeping_hours']

stress_data.isnull().sum()

stress_data.dropna(inplace=True)

stress_data

stress_data.sample()

def conv(text):
  if text=='High':
    return 2
  elif text=='Medium':
    return 1
  elif text=='Low':
    return 0

stress_data['Anxiety_level']=stress_data['Anxiety_level'].apply((lambda x:(conv(x))))
stress_data['Anxiety_level']

stress_data.dropna(inplace=True)

def conv(text):
  if text=='Yes':
    return 1
  elif text=='No':
    return 0

stress_data['Stress_fluctuation']=stress_data['Stress_fluctuation'].apply((lambda x:(conv(x))))
stress_data['Stress_fluctuation']

def conv(text):
  if text=='Yes':
    return 2
  elif text=='Maybe':
    return 1
  elif text=='No':
    return 0

stress_data['Exercise']=stress_data['Exercise'].apply((lambda x:(conv(x))))
stress_data['Exercise']

def conv(text):
  if text=='Yes':
    return 1
  elif text=='No':
    return 0

stress_data['Appearance_change']=stress_data['Appearance_change'].apply((lambda x:(conv(x))))
stress_data['Appearance_change']

def conv(text):
  if text=='High':
    return 2
  elif text=='Moderate':
    return 1
  elif text=='Low':
    return 0

stress_data['Work_load_level']=stress_data['Work_load_level'].apply((lambda x:(conv(x))))
stress_data['Work_load_level']

stress_data.isnull().sum()

def conv(text):
  if text=='Mentally':
    return 2
  elif text=='Both':
    return 1
  elif text=='Physically':
    return 0

stress_data['Stress_type']=stress_data['Stress_type'].apply((lambda x:(conv(x))))
stress_data['Stress_type']

def conv(text):
  if text=='Yes':
    return 1
  elif text=='No':
    return 0

stress_data['Stress']=stress_data['Stress'].apply((lambda x:(conv(x))))
stress_data['Stress']

stress_data.sample()

stress_data.corr()

stress_data.columns

stress_data.info()

stress_data.describe()

stress_data.isnull().sum()

#Extract X and y from the dataframe , income column is the target column, rest␣columns are features
X = stress_data.loc[:,['Age','Anxiety_level', 'Stress_fluctuation',
       'Sleeping_hours', 'Exercise', 'Appearance_change', 'Work_load_level',
       'Stress_type']]
y = stress_data.loc[:,'Stress']

stress_data.columns

X

X.shape

y

from sklearn.svm import SVC
classifier = SVC()
classifier.fit(X,y)

# Example: Model evaluation
from sklearn.metrics import accuracy_score, classification_report
y_pred = classifier.predict(X)
accuracy = accuracy_score(y,y_pred)
print(f'Accuracy: {accuracy:.2f}')
print(classification_report(y,y_pred))

import joblib

joblib.dump(classifier,'model')

!pip install streamlit --quiet

stress_data.dtypes

# Commented out IPython magic to ensure Python compatibility.
# %%writefile svc_model.py
# import streamlit as st
# import joblib
# st.title("WellWiz")
# st.header("Your personal health assistant")
# st.caption("We are using streamlit to build our webapp")
# st.text("Click on Stress Analysis to get your result")
# model=joblib.load("model")
# Age=st.slider('Select your Age:',min_value=15,max_value=31,value=22,step=1)
# Anxiety_level=st.slider('Select the Anxiety_level choose "2" for High "1" for Moderate "0" for Low',min_value=0,max_value=2,value=1,step=1)
# Stress_fluctuation=st.slider('Select the levelof stress Stress_fluctuation ranging from 0 to 1',min_value=0,max_value=1,value=0,step=1)
# Sleeping_hours=st.slider('How many hours do you sleep in a day?',min_value=5,max_value=8,value=6,step=1)
# Exercise=st.slider('Do you exercise--> select the level ranging from 0 to 2:',min_value=0,max_value=2,value=1,step=1)
# Appearance_change=st.slider('Did you observe any changes in your physical appearaance choose "1" for Yes and "0" for no',min_value=0,max_value=1,value=0,step=1)
# Work_load_level=st.slider('Select the level of Work_load choose "2" for High "1" for Moderate "0" for Low',min_value=0,max_value=2,value=0,step=1)
# Stress_type=st.slider('Select the type of stress choose "2" for Mentally "1" for Both "0" for Physically',min_value=0,max_value=2,value=0,step=1)
# 
# if st.button('PREDICT'):
#   op=model.predict([[Age,Anxiety_level,Stress_fluctuation,Sleeping_hours,Exercise,Appearance_change,Work_load_level,Stress_type]])
#   st.subheader(op[0])
#   if op[0]==1:
#     st.subheader("It has been observed that you have stress")
#   elif op[0]==0:
#     st.subheader("It is a relief that you are stress-free")

!streamlit run svc_model.py & npx localtunnel --port 8501

def chatbot_response(input_text):
    # Preprocess user input
    preprocessed_input = X
    # Use the trained model to predict stress level
    stress_prediction = svc_model.predict([preprocessed_input])[0]

    # Determine the response based on stress prediction
    if stress_prediction == 'severe':
        response = "It seems like you might be experiencing severe stress. I strongly recommend seeking professional help."
    else:
        response = "You might be experiencing some stress. I can ask you a few questions to understand better. Are you open to that?"

    return response
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    bot_response = chatbot_response(user_input)
    print("WellWiz: " + bot_response)

!pip install openai

!pip install gradio

import openai
import gradio

openai.api_key="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"
messages=[{"role":"system","content":"You are a personal health assistant for stress management"}]
def CustomerChat(user_input):
  messages.append({"role":"system","content":user_input})
  response=openai.ChatComplete.create

ss.dtype

