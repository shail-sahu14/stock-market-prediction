import streamlit as st
import numpy as np
import pickle as pk

st.title("STOCK MARKET PREDICTION")

st.write(""" 
### TATA MOTORS
Upload volume, open, low, high, close and predict NEXT DAY'S stock price
""")

form = st.form(key='my_form')
volume = form.number_input(label='Enter volume of stock', value=None)
open_price = form.number_input(label='Enter OPENING price of stock', value=None)
close_price = form.number_input(label='Enter CLOSING price of stock', value=None)
high_price = form.number_input(label='Enter HIGHEST price of stock', value=None)
low_price = form.number_input(label='Enter LOWEST price of stock', value=None)
submit_button = form.form_submit_button(label='Submit')


if submit_button:
    if volume==None or open_price==None or close_price==None or high_price==None or low_price==None :
        st.write("""
                 ### Enter realistic value
                 """)
    close_percentage = ((close_price - open_price) / open_price) * 100
    high_percentage = ((high_price - open_price) / open_price) * 100
    low_percentage = ((low_price - open_price) / open_price) * 100

    test_input = np.array([volume, close_percentage, high_percentage, low_percentage]).reshape(1, 4)
    pipe = pk.load(open('pipe.pkl','rb'))
    nextday_percentage = pipe.predict(test_input)
    nextday_price = open_price+(nextday_percentage/100)*open_price
    st.write(f"Next day's stock price prediction: {nextday_price[0]}")
