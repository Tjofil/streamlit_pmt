from turtle import width
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
def load_data(nrows):
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
    data = load_data(50000)
    data = data.drop('Unnamed: 0', axis = 1)
    data_load_state.text('Finished fetching data!')
    st.subheader('Raw data')
    st.write(data, width=100)
    
    hist_data = [data['BMI'], data['Age']]
    group_labels = ['BMI', 'Age']
    # fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])

    categorical_val = [column for column in data.columns if len(data[column].unique()) <= 5]
    continous_val = [column for column in data.columns if len(data[column].unique()) > 5]

    import plotly.graph_objects as go
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=data[data['Diabetes_binary'] == 0]['BMI'], name = 'Have diabetes = NO'))
    fig.add_trace(go.Histogram(x=data[data['Diabetes_binary'] == 1]['BMI'], name = 'Have diabetes = YES'))
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)

    st.subheader('Diabetes cases per BMI distribution')
    st.plotly_chart(fig, use_container_width = True)
    
    # Let's make our correlation matrix a little prettier
    corr_matrix = data.corr()
    fig_corr =px.imshow(corr_matrix,
        labels = dict(color = 'Productivity'),
        x = data.columns,
        y = data.columns
    )
    st.subheader('Correlation of health attributes')    
    st.plotly_chart(fig_corr, use_container_width=True)
    
    
    # fig, ax = plt.subplots(figsize=(15, 15))
    # ax = sns.heatmap(corr_matrix,
    #                  annot=True,
    #                  linewidths=0.5,
    #                  fmt=".2f",
    #                  cmap="YlGnBu")
    # bottom, top = ax.get_ylim()
    # ax.set_ylim(bottom + 0.5, top - 0.5)
    



    