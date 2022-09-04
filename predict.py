import json
import streamlit as st
import requests as rq

def predict(features):
    return json.loads(rq.post('https://desolate-oasis-06152.herokuapp.com/predict', json=features).content)['Outcome']
    

def display_predict_page():
    st.title('Diabetes prediction using Machine Learning')
    st.write('''### Plug in your health information to predict the disease.''')

    high_bp = st.checkbox('Do you have high blood preasure ?', value = False)
    st.write('>Having 130 or more for systolic and 80 or more for diastolic blood pressure is considered having a high blood pressure')

    high_chol = st.checkbox('Do you have high cholesterol ?', value = False)
    st.write('>Having 240 or more for total cholesterol level is considered having a high cholesterol')
    bmi = st.slider('Body mass index', max_value= 98, min_value= 12)
    st.write('>[Find about and calculate your BMI.](https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm)')
    smoker = st.checkbox('Have you smoked at least 100 cigarettes in your entire life ?', value = False)
    stroke = st.checkbox('Have you experienced a stroke in your life ?', value = False)
    heart = st.checkbox('Have you experienced a heart attack or suffering from heart diseases ?', value = False)
    phys_act = st.checkbox('Have you had any physical activity in past 30 days?', value = False)
    fruits = st.checkbox('Do you consume at least one fuit per day ?', value = False)
    veggies = st.checkbox('Do you consume at least one vegetable per day ?', value = False)
    hvy_alcohol = st.checkbox('Do you practice heavy alcohol consumption ?', value = False)
    diff_walk = st.checkbox('Do you any difficulties walking ?', value = False)
    st.write('>Consuming at least 14 for men and at least 7 for women alcoholic drinks per week is considered heavy alcohol consumption.')
    age = st.number_input('Your age', value= 24)
    age_category = 1 if age<= 24 else 2 + (age - 25)//5

    menth_hlth = st.slider('Number days of poor mental health in previous 30 days', min_value = 0, max_value = 30)
    phys_htlh = st.slider('Number days of poor physical health in previous 30 days', min_value = 0, max_value = 30)

    features = {
    "HighBP":                 high_bp,
    "HighChol":               high_chol,
    "BMI":                    bmi,
    "Smoker":                 smoker,
    "Stroke":                 stroke,
    "HeartDiseaseorAttack":   heart,
    "PhysActivity":           phys_act,
    "Fruits":                 fruits,
    "Veggies":                veggies,
    "HvyAlcoholConsump":      hvy_alcohol,
    "MentHlth":               menth_hlth,
    "PhysHlth":               phys_htlh,
    "DiffWalk":               diff_walk,
    "Age":                    age_category
    }

    calc = st.button('Calculate the diabetes prediction')
    if calc:
        prediction = predict(features)
        st.subheader(f'The model has predicted that you {"" if prediction else "dont"} have diabetes')




