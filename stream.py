import streamlit as st 
import pandas as pd
import numpy as np
from predict import display_predict_page

st.sidebar.selectbox('Explore or predict the data', ('Explore', 'Predict'))

display_predict_page()


# st.title('Predicting diabetes using Machine Learning')



# Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# # Load 10,000 rows of data into the dataframe.
# data = load_data(1000)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text('Done! (using st.cache)')

# st.subheader('Raw data')
# st.write(data)

# data_load_state.text('Done 2 !')
# hist_values = np.histogram(
#     data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

# st.bar_chart(hist_values)

# hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# st.map(filtered_data)
