import streamlit as st
import pandas as pd
import numpy as np
from predict_page import predict_fn
from explore_page import explore_fn
from Home_page import home_fn

temp=st.sidebar.selectbox("EXPLORE OR PREDICT",("Home","Predict","Explore"),0)
if temp=="Predict":
    st.sidebar.write("Predict if employee stays in the company or not")
    predict_fn()
    
elif temp=="Explore":
    st.sidebar.write("Visualization through visual imagery has been an effective way to communicate both abstract and concrete ideas since the dawn of humanity.")
    explore_fn()
else:
    home_fn()
