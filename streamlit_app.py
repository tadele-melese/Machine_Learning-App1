import streamlit as st
import pandas as pd

st.title('🎈 Machine Learning App ')

st.info('This app builds machine learning model')
with st.expander('Data'):
  st.write('**Main Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/tadele-melese/Machine_Learning-App1/master/climate.csv')
  df

st.write('**X**')
X=df.drop('SPI', axis = 1)
X
st.write('**Y**')
Y =df.SPI
Y
