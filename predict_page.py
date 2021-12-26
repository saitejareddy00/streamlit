import streamlit as st
import pandas as pd
import numpy as np
def predict_fn():
    st.title("Employee Attrition Prediction")
    st.write("### We Need some information to predict if the employee stays in the company or not ###")
    jobroles=["Healthcare Representative","Human Resources","Laboratory Technician","Manager","Manufacturing Director","Research Director","Research Scientist","Sales Executive","Sales Representative"]
    jr=st.selectbox("JOB ROLE",jobroles,7)



    edufields=["Human Resources","Life Sciences","Marketing","Medical","Other","Technical Degree"]
    ef=st.selectbox("EDUCATION FIELD",edufields,1)

    travel=("Non-Travel","Travel_Frequently","Travel_Rarely")
    business=st.selectbox("BUSINESS_TRAVEL",travel,2)

    dept=["Human Resources","Research & Development","Sales"]
    dep=st.selectbox("DEPARTMENT",dept,2)

    gen=["Female","Male"]
    gender=st.selectbox("Gender",gen)

    marriage=["Divorced","Married","Single"]
    maritialstatus=st.selectbox("MaritalStatus",marriage,2)

    test=pd.read_csv('testdata1.csv')
    bigli=[]
    columns11=list(test.columns)

    dic={"StandardHours":80,"EmployeeCount":1}
    for i in test.iloc[:1,0:26]:
        if i=="EmployeeCount" or i=="StandardHours":
            bigli.append(dic[i])
        else:
            max=test[i]
            max1,min1=np.max(max),np.min(max)
            temp=st.selectbox(i,range(int(min1),int(max1)+1))
            bigli.append(temp)
    ot=["yes","no"]
    over=1
    overtime=st.selectbox("OverTime",ot)
    temp=[travel,dept,edufields,gen,jobroles,marriage,over,ot]
    values=[business,dep,ef,gender,jr,maritialstatus,over,overtime]
    for val,lis in zip(values,temp):
        if val!=1:
            temlis=[0]*len(lis)
            temlis[lis.index(val)]=1
            bigli+=temlis
        else:
            bigli.append(1)
    a=st.button("okok")

    if a:
        lst=[bigli]
        print("lengths of list and test",len(bigli),len(columns11))
        newdf=pd.DataFrame(lst,columns=columns11,dtype=np.int64)

        import pickle
        filename = 'finalized_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        print("ans",loaded_model.predict(newdf))
        
