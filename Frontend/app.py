import streamlit as st
import requests as re
import json

st.write("""# Credit Card Fraud Detection Web App""")

st.image("image.png")

st.write("""
## About

Credit card fraud is a form of identity theft that involves an unauthorized taking of another's credit card information for the purpose of charging purchases to the account or removing funds from it.

**This Streamlit App utilizes a Machine Learning API in order to detect fraudulent credit card  based on the following criteria: age, gender, blood pressure, smoke, coughing, allergies, fatigue etc.** 

The notebook, processed dataset, model and documentation(Dockerfiles, FastAPI script, Streamlit App script) are available on [GitHub.](https://github.com/Nneji123/Credit-Card-Fraud-Detection)        

**Made by Group 3 Zummit Africa Team**

**Contributors: Hilary Ifezue(Group Lead)
                Nneji Ifeanyi
                Somtochukwu Ogechi
                ThankGod Omieje
**
""")


st.sidebar.header('User Input Features')


gender = st.sidebar.number_input("GENDER: Enter 1 for Male and 0 for Female", min_value=0, max_value=1)
age = st.sidebar.slider("AGE: Enter your Age", min_value=1, max_value=100)
smoking = st.sidebar.number_input("SMOKING: Enter 1 if you smoke or 0 if you don't smoke", min_value=0, max_value=1)
yellow_finger = st.sidebar.number_input("YELLOW FINGERS: Enter 1 if you have yellow fingers or 0 if you don't", min_value=0, max_value=1)
anxiety = st.sidebar.number_input("ANXIETY: Enter 1 if you have anxiety and 0 if you don't", min_value=0, max_value=1)
peer = st.sidebar.number_input("PEER PRESSURE: Enter 1 if you feel you suffer from peer pressure or 0 if you don't", min_value=0, max_value=1)
chronic = st.sidebar.number_input("CHRONIC DISEASE: Enter 1 if you suffer from a chronic disease or O if you don't", min_value=0, max_value=1)
fatigue = st.sidebar.number_input("FATIGUE: Enter 1 if you have fatigue or 0 if you don't", min_value=0, max_value=1)
allergy = st.sidebar.number_input("ALLERGY: Enter 1 if you have some sort of allergy or 0 if you don't", min_value=0, max_value=1)
wheezing = st.sidebar.number_input("WHEEZING: Enter 1 if you wheeze or 0 if you don't", min_value=0, max_value=1)
alcohol =  st.sidebar.number_input("ALCOHOL CONSUMPTION: Enter 1 if you consume alcohol or 0 if you don't", min_value=0, max_value=1)
coughing = st.sidebar.number_input("COUGHING: Enter 1 if you cough a lot or 0 if you don't", min_value=0, max_value=1)
breath = st.sidebar.number_input("SHORTNESS OF BREATH: Enter 1 if you suffer from shortness of breath or 0 if you don't", min_value=0, max_value=1)
swallow =  st.sidebar.number_input("SWALLOWING DIFFICULTY: Enter 1 if you have difficulty swallowing or 0 if you don't", min_value=0, max_value=1)
chest =  st.sidebar.number_input("CHEST PAIN: Enter 1 if you have chest pain or 0 if you don't", min_value=0, max_value=1)



if st.button('Detection Result'):
    values =  {
    
    "GENDER": gender,
    "AGE": age,
    "SMOKING": smoking,
    "YELLOW_FINGERS": yellow_finger,
    "ANXIETY": anxiety,
    "PEER_PRESSURE": peer,
    "CHRONIC_DISEASE": chronic,
    "FATIGUE": fatigue,
    "ALLERGY": allergy,
    "WHEEZING": wheezing,
    "ALCOHOL_CONSUMPTION": alcohol,
    "COUGHING": coughing,
    "SHORTNESS_OF_BREATH": breath,
    "SWALLOWING_DIFFICULTY": swallow,
    "CHEST_PAIN": chest
    }
    res = re.post(f"http://backend.docker:8000/predict", json=values)
    json_str = json.dumps(res.json())
    resp = json.loads(json_str)

    st.write(resp[0])