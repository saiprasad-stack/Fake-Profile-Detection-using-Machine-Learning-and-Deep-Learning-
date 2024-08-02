import numpy as np
import pickle
import pandas as pd
import streamlit as st

import joblib

model = joblib.load("classifier.pkl")


def predictor(postsCount,followersCount,followsCount,private,verified):
    prediction = model.predict([[postsCount,followersCount,followsCount,private,verified]])
    print(prediction)
    return prediction


def main():
    st.title("Fake Instagram Profile Detection")
    st.write("Plaese provide instagram account details you would like to predict")
    postsCount = st.text_input("Number of Posts")
    followersCount = st.text_input("Number of Followers")
    followsCount = st.text_input("Number of Following")
    private = st.text_input("Is account private or not (provide in 0 or 1)")
    verified = st.text_input("Is account verified or not (provide in 0 or 1)")
    if st.button("Predict"):
        result = predictor(postsCount,followersCount,followsCount,private,verified)
        if result==0:
            st.success("The Account is Likely to be Fake ")
        else:
            st.success("The Account is Likely to be Real")


if __name__=='__main__':
    main()