import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def home_fn():
    st.title("Employee Attrition Prediction with Python")
    st.write("Machine Learning Project on Employee Attrition Prediction with Python")
    st.write("Employee attrition is downsizing in any organization where employees resign. Employees are valuable assets of any organization. It is necessary to know whether the employees are dissatisfied or whether there are other reasons for leaving their respective jobs.")
    st.write("Nowadays, for better opportunities, employees are eager to move from one organization to another. But if they quit their jobs unexpectedly, it can result in a huge loss for the organization. A new hire will consume money and time, and newly hired employees will also take time to make the respective organization profitable.")
    components.html("<a target = blank class=\"wp-block-button__link\" href=\"https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset/download\">Download Dataset</a>")