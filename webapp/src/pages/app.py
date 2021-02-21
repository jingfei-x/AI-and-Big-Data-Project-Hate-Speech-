"""Main module for the streamlit app"""

# importing relevant python packages
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import re
import string
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from sklearn.feature_extraction.text import TfidfVectorizer

def write():
    tweet_input = st.beta_container()
    model_results = st.beta_container()
    contact = st.beta_container()

    with tweet_input:
        st.header('Is Your Tweet Considered Hate Speech?')
        user_text = st.text_input('Write the Tweet', max_chars=280) # setting input as user_text


    with model_results:    
        if st.button("Predict"): 
            # removing punctuation
            user_text = re.sub('[%s]' % re.escape(string.punctuation), '', user_text)
            # tokenizing
            stop_words = set(stopwords.words('english'))
            tokens = nltk.word_tokenize(user_text)
            # removing stop words
            stopwords_removed = [token.lower() for token in tokens if token.lower() not in stop_words]
            # taking root word
            lemmatizer = WordNetLemmatizer() 
            lemmatized_output = []
            for word in stopwords_removed:
                lemmatized_output.append(lemmatizer.lemmatize(word))

            # instantiating count vectorizor
            tfidf = TfidfVectorizer()
            X_train = pickle.load(open('pickle/X_train.pkl', 'rb'))
            X_test = lemmatized_output
            X_train_count = tfidf.fit_transform(X_train)
            X_test_count = tfidf.transform(X_test)

            # loading in model
            final_model = pickle.load(open('pickle/final_logreg_model.pkl', 'rb'))

            # apply model to make predictions
            prediction = final_model.predict(X_test_count[0])

            if prediction == 0:
                st.error('**Hate Speech  :anger:**')
            elif prediction == 1:
                st.warning('**Offensive Language  :collision:**')
            else:
                st.success('**Neither  :smiley:**')
            st.text('')
            



