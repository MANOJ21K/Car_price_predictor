### importing the necesdary packages
import streamlit as st
import pickle
import numpy as np


# function for the model 
def load_model():
    with open('saved_steps.pkl','rb') as file:
        data=pickle.load(file)
    return data

data=load_model()


#assigning the label encoders and model
regressor = data['model']
le_Brand = data['Brand']
le_Body = data['Body']
le_Engine_Type = data['Engine_Type']
le_Registration = data['Registration']


#creating the prediction page
def show_predict_page():
    st.title("Used Car Price Prediction")


    st.write("### Need some information to predict the price")


    Brand=('BMW', 'Mercedes-Benz', 'Audi', 'Toyota', 'Renault', 'Volkswagen',
       'Mitsubishi')

    Body=('sedan', 'van', 'crossover', 'vagon', 'other', 'hatch')   

    Engine_Type =('Petrol','Diesel','Gas','Other')

    Registration=('yes','no')

    Brand = st.selectbox("Brand",Brand)

    Body = st.selectbox("Body",Body)

    Engine_Type = st.selectbox("Engine Type",Engine_Type)

    Registration = st.selectbox("Registered or not",Registration)

    EngineV=st.slider("Engine Volume",0,7,2)

    Mileage =st.slider("Kms travelled",0,1000,100)



    ok = st.button("Calculate price")

    if ok:
        df= np.array([[Brand,Body,Engine_Type,Registration,EngineV,Mileage]])
        df[:, 0] = le_Brand.transform(df[:,0])
        df[:, 1] = le_Body.transform(df[:,1])
        df[:, 2] = le_Engine_Type.transform(df[:,2])
        df[:, 3] = le_Registration.transform(df[:,3])
        df = df.astype(float)


        price = regressor.predict(df)
        Price=np.exp(price)
        st.subheader(f"The estimated price for the car is ${Price[0]:.2f}")

