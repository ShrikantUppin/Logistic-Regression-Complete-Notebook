
import streamlit as st
import pickle
import gzip
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

infile1 = open('fianl_model.p','rb')
final_model = pickle.load(infile1)
infile1.close()

infile2 = open('country_codes1.p','rb')
country_codes = pickle.load(infile2)
infile2.close()

infile3 = open('city_codes1.p','rb')
city_codes = pickle.load(infile3)
infile3.close()

infile4 = open('country_city_dict.p','rb')
country_city_dict = pickle.load(infile4)
infile3.close()

city_df = pd.DataFrame(list(city_codes.items()), columns=['City','Code'], index=[i for i in range(1,len(city_codes)+1)])
country_df = pd.DataFrame(list(country_codes.items()),columns=['Country','Code'], index=[i for i in range(1,len(country_codes)+1)])

def inputs(Daily_Time_Spent_on_Site, Age, Area_Income,Daily_Internet_Usage, City, Male, Country):
    
    new_data=pd.DataFrame({'Daily_Time_Spent_on_Site':Daily_Time_Spent_on_Site,"Age":Age,"Area_Income":Area_Income, "Daily_Internet_Usage":Daily_Internet_Usage,
                           "City":City, "Male":Male, "Country":Country},index=[1])
   
    new_data[["Daily_Time_Spent_on_Site","Area_Income","Daily_Internet_Usage"]] = new_data[["Daily_Time_Spent_on_Site","Area_Income","Daily_Internet_Usage"]].astype('float')
    
    new_data[["Age","City","Male","Country"]] = new_data[["Age","City","Male","Country"]].astype('int')
    

    final_predict = final_model.predict(new_data)
    
    return final_predict
    
    

def final():
    
    st.title('Logistic Regression')
    '''#### Predicting user has clicked on Advertise or not!'''
    '''Dataset : advertising.csv'''
    '''@ Shrikant Uppin'''
    '''***'''
    st.markdown("![Image](https://github.com/ShrikantUppin/Logistic-Regression-Complete-Notebook/blob/main/ppc.png?raw=true)")
    st.text('image source: https://www.softechpro.in/img/ppc.png')
    # Daily_Time_Spent_on_Site
    Daily_Time_Spent_on_Site = st.sidebar.number_input('Daily Time Spent in Minutes', 32, 92)
    
    
    # Area Income
    Area_Income = st.sidebar.number_input('Area income in USD',10000,80000)
    
    # Daily_Internet_Usage
    Daily_Internet_Usage = st.sidebar.number_input('Daily Internet Usage',100, 300)
    
    # Male
    male = st.sidebar.selectbox('Select Gender', ['Male','Female'])
    if male == 'Male':
        Male = 1
    else:
        Male =0
    
      # Age of the user
    Age = st.sidebar.number_input("Age of the user", 19, 60, 40)
    
     # getting code value for entered country & reassigning to it Coutry variable in function.
    country = st.sidebar.selectbox('Select Country', country_df.Country.unique())
    search1 = country
    a = country_df.loc[country_df.isin([search1]).any(axis=1)].index.values
    b = country_df.Code.loc[a].values
    Country = b
    
    #Similar for cities..when selected particular country then automatic cities
    #... in that country will be displayed to select.
    city = st.sidebar.selectbox('Select City', list(country_city_dict.get(search1)))
    c = city_df.loc[city_df.isin([city]).any(axis=1)].index.values
    d = city_df.Code.loc[c].values
    City = d
   
    sample_data = inputs(Daily_Time_Spent_on_Site, Age, Area_Income,Daily_Internet_Usage, City, Male, Country)       
    
    
    if st.button('predict'):
        output = inputs(Daily_Time_Spent_on_Site, Age, Area_Income,Daily_Internet_Usage, City, Male, Country)
        if output ==1:
            st.success("'{}' User clicked on Advertise".format('YES'))
        else:
            st.success("'{}' User clicked on Advertise".format('NO'))

final()
    