
    
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

sell_saved_model = pickle.load(open('sell_saved_model.sav', 'rb'))






    
# sell into strength  Prediction Page
if (selected == 'Sell into Strength Prediction'):
    
    # page title
    st.title('Sell into Strength Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(2)
    
    with col1:
        three_day_returns = st.text_input('Percentage of last three day candles distance')
        
    with col2:
        four_day_returns = st.text_input('Percentage of last four day candles distance')
    
    with col3:
        five_day_returns = st.text_input('Percentage of last five day candles distance')
    
    with col1:
        ema_distance = st.text_input('Percentage of distance from 21 EMA to last candle ')
    
    with col2:
        exhausion_days = st.text_input('Number of exhausion gaps in last five days')
    
    
    
    # code for Prediction
    sell_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Advice'):
        sell_prediction = sell_saved_model.predict([[three_day_returns,four_day_returns,five_day_returns,ema_distance,exhausion_days]])
        
        if (sell_prediction[0] == 1):
          diab_diagnosis = 'Enjoy the rides and keep trailing stop loss'
        else:
          diab_diagnosis = 'Safe players can book profits'
        
    st.success(sell_diagnosis)
