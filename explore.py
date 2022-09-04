import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import hvplot.pandas
import seaborn as sns
import plotly.express as px


sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")


@st.cache
def load_data():
    raw_data = requests.get('https://desolate-oasis-06152.herokuapp.com/dataset')
    open('local.csv', 'wb').write(raw_data.content)
    data = pd.read_csv('local.csv')
    # lowercase = lambda x: str(x).lower()
    # data.rename(lowercase, axis='columns', inplace=True)
    return data

def display_explore_page():
    st.title('Explore the diabetes study data.')

    st.write(
        """
        ### Diabetes tests based on personal health data.
        """
    )
    data_load_state = st.text('Loading data...')
    data = load_data()
    data = data.drop('Unnamed: 0', axis = 1)
    data_load_state.text('Finished fetching data!')
    st.subheader('Raw data')
    st.write(data, width=1000)
    
    import plotly.graph_objects as go
    fig_bmi = go.Figure()
    fig_bmi.add_trace(go.Histogram(x=data[data['Diabetes_binary'] == 0]['BMI'], name = 'Have diabetes = NO'))
    fig_bmi.add_trace(go.Histogram(x=data[data['Diabetes_binary'] == 1]['BMI'], name = 'Have diabetes = YES'))
    fig_bmi.update_layout(barmode='overlay', xaxis_title_text='Body mass index', yaxis_title_text='Count')
    fig_bmi.update_traces(opacity=0.6)

    st.subheader('Diabetes cases per BMI distribution')
    st.plotly_chart(fig_bmi, use_container_width = True)
    
    fig_income = go.Figure()
    fig_income.add_trace(go.Histogram(x=data[data['Diabetes_binary'] == 0]['Income'], name = 'Have diabetes = NO'))
    fig_income.add_trace(go.Histogram(x=data[data['Diabetes_binary'] == 1]['Income'], name = 'Have diabetes = YES'))
    fig_income.update_layout(barmode='overlay', xaxis_title_text='Income category', yaxis_title_text='Count')
    fig_income.update_xaxes(type='category')
    fig_income.update_traces(opacity=0.6)

    st.subheader('Confirmed diabetes cases per household income category.')

    st.plotly_chart(fig_income, use_container_width = True)
    st.write(""">Household income categories are calculated as following:
    Category: 1 -> less than 10k USD annual income.
    Category: 2 -> less than 15k USD annual income.
                    ...
    Category: 7 -> less than 75k USD annaul income.
    Category: 8 -> more or equal than 75k USD annual income.
    """)
    # Correlation matrix of all dataset columns

    fig_mental = go.Figure()
    fig_mental.add_trace(go.Histogram(x=data[data['Diabetes_binary'] == 0]['MentHlth'], name = 'Have diabetes = NO'))
    fig_mental.add_trace(go.Histogram(x=data[data['Diabetes_binary'] == 1]['MentHlth'], name = 'Have diabetes = YES'))
    fig_mental.update_layout(barmode='overlay', xaxis_title_text='Days with mental health issues during last month', yaxis_title_text='Count')
    fig_mental.update_traces(opacity=0.6)

    st.subheader('Confirmed diabetes cases per mental health issues in last 30 days')
    st.plotly_chart(fig_mental, use_container_width = True)

     
    corr_matrix = data.corr()
    fig_corr =px.imshow(corr_matrix,
        labels = dict(color = 'Correlation'),
        x = data.columns,
        y = data.columns
    )

    st.subheader('Correlation of all dataset columns') 
    st.plotly_chart(fig_corr, use_container_width=True)
    

    
    

    



    