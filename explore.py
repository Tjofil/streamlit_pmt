import streamlit as st
import pandas as pd
import requests

@st.cache
def load_data(nrows):
    raw_data = requests.get('https://desolate-oasis-06152.herokuapp.com/dataset')
    open('local.csv', 'wb').write(raw_data.content)
    data = pd.read_csv('local.csv', nrows=nrows)
    # lowercase = lambda x: str(x).lower()
    # data.rename(lowercase, axis='columns', inplace=True)
    return data

def display_explore_page():
    st.title('Explore data ')