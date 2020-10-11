# Section 1: Import required Libraries...

import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

#------------------------------------------------------------------

# Section1: Unpickle all pickled data form jupyter notebook...

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

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Section 2: From unpickled infile 4, Generating different dataframes for city & country names
#            this will helpful during writing streamlit codes.

city_df = pd.DataFrame(list(city_codes.items()), columns=['City','Code'], index=[i for i in range(1,len(city_codes)+1)])
country_df = pd.DataFrame(list(country_codes.items()),columns=['Country','Code'], index=[i for i in range(1,len(country_codes)+1)])

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Section 3: Writing function which will return prediction:
    
def inputs(Daily_Time_Spent_on_Site, Age, Area_Income,Daily_Internet_Usage, City, Male, Country):
    
    new_data=pd.DataFrame({'Daily_Time_Spent_on_Site':Daily_Time_Spent_on_Site,"Age":Age,"Area_Income":Area_Income, "Daily_Internet_Usage":Daily_Internet_Usage,
                           "City":City, "Male":Male, "Country":Country},index=[1])
   
    new_data[["Daily_Time_Spent_on_Site","Area_Income","Daily_Internet_Usage"]] = new_data[["Daily_Time_Spent_on_Site","Area_Income","Daily_Internet_Usage"]].astype('float')
    new_data[["Age","City","Male","Country"]] = new_data[["Age","City","Male","Country"]].astype('int')
    final_predict = final_model.predict(new_data)
    
    return final_predict
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

# Writing Streamlit webpage section ...this will displayed on web/taking inputs from user etc.

def to_be_display():
    
    #--------------------------this will be displayed on main page-----------------------------
    
    st.title('Logistic Regression Model Deployment')
    '''## Predicting user has clicked on Advertise or not!'''
    '''Dataset : advertising.csv'''
    '''@ Shrikant Uppin'''
    '''***'''
    #------------------------------------------------------------------------------------------
    #-------------------------displayed in sidebar of webpage app------------------------------
    # Writing treamlit code to take inputs from user & assign it to inputs() function.
    
    st.sidebar.title('Provide Inputs:')
    
    Daily_Time_Spent_on_Site = st.sidebar.number_input('Daily Time Spent in Minutes', 32, 92)
    Area_Income = st.sidebar.number_input('Area income in USD',10000,80000)
    Daily_Internet_Usage = st.sidebar.number_input('Daily Internet Usage',100, 300)
    
    #---------------------------------------------------------------
    # Writing mini-inside loop to assign value to Male variable.
    
    male = st.sidebar.selectbox('Select Gender', ['Male','Female'])
    if male == 'Male':
        Male = 1
    else:
        Male =0
    #---------------------------------------------------------------
    
    Age = st.sidebar.number_input("Age of the user", 19, 60, 40)
    
    # getting code value for entered country & reassigning to it Coutry variable in function.
    
    country = st.sidebar.selectbox('Select Country', country_df.Country.unique())
    search1 = country
    a = country_df.loc[country_df.isin([search1]).any(axis=1)].index.values
    b = country_df.Code.loc[a].values
    Country = b
    
    #--------------------------
    city = st.sidebar.selectbox('Select City', list(country_city_dict.get(search1)))
    c = city_df.loc[city_df.isin([city]).any(axis=1)].index.values
    d = city_df.Code.loc[c].values
    City = d
    
    #--------------------------this will be displayed on main page-----------------------------
    ''' ### Want to check how ref. raw data looks..?'''
    if st.button('Raw Data'):
        raw_data = pd.read_csv('advertising.csv')
        st.write(raw_data.head())
    '''***'''
    st.write()
    ''' ### Have you provided Inputs..? Let's predict Yes/No..!!!''' 
    '''   '''
    if st.button('predict'):
        output = inputs(Daily_Time_Spent_on_Site, Age, Area_Income,Daily_Internet_Usage, City, Male, Country)
        if output ==1:
            st.write(' ### User clicked on Advertise..!!!')
            st.markdown("![Image](https://github.com/ShrikantUppin/Logistic-Regression-Complete-Notebook/blob/main/yes.gif?raw=true)")
        else:
            st.markdown("![Image](https://github.com/ShrikantUppin/Logistic-Regression-Complete-Notebook/blob/main/no.gif?raw=true)")
    ''' *** '''

    link = '[Click here for source code..!](https://github.com/ShrikantUppin/Logistic-Regression-Complete-Notebook)'
    st.markdown(link, unsafe_allow_html=True)
    
    '''***'''
    
    link = '[Fallow me on GitHub](https://github.com/ShrikantUppin)'
    st.markdown(link, unsafe_allow_html=True)
    
#------calling to_be_display() function------------------------

to_be_display()

#--------------------------------end of the code------------------------------------------------
    