import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

predict = pickle.load(open( "predict.p", "rb" ))

def inputs(Daily_Time_Spent_on_Site, Age, Area_Income,Daily_Internet_Usage, City, Male, Country):
    
    new_data=pd.DataFrame({'Daily_Time_Spent_on_Site':Daily_Time_Spent_on_Site,"Age":Age,"Area_Income":Area_Income, "Daily_Internet_Usage":Daily_Internet_Usage,
                           "City":City, "Male":Male, "Country":Country},index=[1])
    
    new_data[[" Daily_Time_Spent_on_Site","Area_Income","Daily_Internet_Usage"]] = df[[" Daily_Time_Spent_on_Site","Area_Income","Daily_Internet_Usage"]].astype('float')
    
    new_data[["Age","City","Male","Country"]] = df[["Age","City","Male","Country"]].astype('int')
    final_predict = final_model.predict(new_data)
    return(final_predict).values

def main():
    
    st.title('Logistic Regression')
    '''#### Predicting user has clicked on Advertise or not!'''
    '''Dataset : advertising.csv'''
    '''@ Shrikant Uppin'''
    
    
    
if __name__=='__main__':
        main()
    