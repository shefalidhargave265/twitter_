# install streamlit: pip install streamlit
# run: streamlit run app.py

import streamlit as st
import pickle
import time
 
# load the model
model = pickle.load(open('D:\New_Twitter sentiment\Twitter-sentiment-analysis-using-Python-Machine-Learning-Project-8-main\twitter_sentiment_model.pkl', 'rb'))

st.title('Twitter Sentiment Analysis')

tweet = st.text_input('Enter your tweet')

submit = st.button('Predict')

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write('Prediction time taken: ', round(end-start, 2), 'seconds')
    
    print(prediction[0])
    st.write(prediction[0])