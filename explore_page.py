import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def explore_fn():
    df=pd.read_csv("Employee-Attrition.csv")
    df = df.drop('EmployeeNumber', axis = 1) # A number assignment 
    #Remove the column StandardHours
    df = df.drop('StandardHours', axis = 1) #Contains only value 80 
    #Remove the column EmployeeCount
    df = df.drop('EmployeeCount', axis = 1) #Contains only the value 1 
    #Remove the column EmployeeCount
    df = df.drop('Over18', axis = 1)
    attrition=df
    columns11=list(df.columns)
    
    st.title("Explore The Trends In Attrition")

    attr=st.selectbox("select Attribute you want vs Attrition",columns11,0)

    '''
    attr2=st.multiselect("choose attribute",columns11)
    data=df[attr2]
    st.line_chart(data)'''
    fig_dims = (24,12)
    fig3, ax = plt.subplots(figsize=fig_dims)
    sns.countplot(x=attr, hue='Attrition', data = df, palette="colorblind", ax = ax,  edgecolor=sns.color_palette("dark", n_colors = 1))
    plt.title("employees that left and stayed by "+attr)
    st.pyplot(fig3)

    st.write("better visual of the correlation by using a heat map.")
    corr=plt.figure(figsize=(14,14))  #14in by 14in
    sns.heatmap(df.corr(), annot=True, fmt='.0%')
    st.pyplot(corr)
    