import streamlit as st
import pandas as pd
import pickle
import string
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path


import os
filepath = 'C:/Usersntc/Downloads/MVPR/price.pkl'
if os.path.exists(filepath):
    file = open('C:/Usersntc/Downloads/MVPR/price.pkl', 'rb')
    codedata = pickle.load(file)
    file.close()
else:
    print("File not present at desired location")



def main():
    # Title
    st.title('Hi there! Welcome to the USA House Price Predictor')

    # header
    st.header('Fill out the following then press submit to get a rough estimate of what your house could be bought/sold for!')

    option = st.selectbox('State',
    ('Connecticut', 'Massachusetts', 'New York', 'Pennsylvania', 'New Jersey', 'Comedy', 'Mystery',))
    # no. of beds slider
    beds = st.slider(label='Number of Bedrooms', max_value=10)

    # no. of bathrooms slider
    baths = st.slider(label='Number of Bathrooms', max_value=10)

    #Total sqft slider
    size = st.number_input(label='Total size of the house in Sqft', max_value=30000)



    

    inputs = [[beds, baths, size]]

    my_list = ["20000 USD", "568888 USD", "50000 USD"]
    show_price = st.button("submitt")

# Initialize the current index
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0
   
# Whenever someone clicks on the button
    if show_price:
        st.write(my_list[st.session_state.current_index])
    # Update and store the index
        st.session_state.current_index += 1
if __name__ =='__main__':
    main()
