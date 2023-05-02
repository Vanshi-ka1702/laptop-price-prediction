import streamlit as st
import pickle
import numpy as np

pipe= pickle.load(open('laotop.pkl','rb'))
df=pickle.load(open('pipe.pkl','rb'))
#company
st.title("Laptop Price Prediction")

#brand
Company = st.selectbox('Brand',pipe['Company'].unique())

# type of pipe  
type = st.selectbox('Type',pipe['Type'].unique()) 

#Ram
Ram = st.selectbox('Ram' ,pipe['Ram'].unique())

#weight
weight = st.number_input('Weight of the Laptop')


#touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

#IPS
ips = st.selectbox('Ips',['No','Yes'])

#screen size
screen_size = st.number_input('Screen Size')

#resolution
resolution= st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
cpu = st.selectbox('CPU',pipe['Cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',pipe['Gpu brand'].unique())

os = st.selectbox('OS',pipe['os'].unique())

if st.button('Predict Price'): 
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([Company,type,Ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(df.predict(query)[0]))))


    

