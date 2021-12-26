import streamlit as st
import pandas as pd
import numpy as np
from predict_page import predict_fn
from explore_page import explore_fn

temp=st.sidebar.selectbox("EXPLORE OR PREDICT",("Predict","Explore"),1)
if temp=="Predict":
    predict_fn()
    st.sidebar.write("Predict if employee stays in the company or not")
else:
    explore_fn()
    st.sidebar.write("Visualization through visual imagery has been an effective way to communicate both abstract and concrete ideas since the dawn of humanity.")
