# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:08:37 2024

@author: Pratik
"""

import pickle
import streamlit as st

st.title('Customer_Segment Using Clustering Algorithms :bar_chart:')

load = open('Segment_model.pkl', 'rb')
model = pickle.load(load)

def predict(Gender,Age,Annual_Income,Spending_score):
    prediction = model.predict([[Gender,Age,Annual_Income,Spending_score]])
    return prediction

def main():
    
    st.markdown('This is to predict which group customer belongs!!!')
    Gender = st.selectbox('Gender',('Male','Female'))
    Age = st.number_input('Age',min_value= 0,max_value= 80)
    Annual_Income = st.number_input('Annual_Income ($)',max_value= 100)
    Spending_score = st.number_input('Spending_Score ($)',max_value= 100)
    if st.button('Predict'):
        result = predict(Gender,Age,Annual_Income,Spending_score)
        st.success('Belongs to group : {} '.format(result))
        
        
        
if __name__ == '__main__':
    main()
      

    