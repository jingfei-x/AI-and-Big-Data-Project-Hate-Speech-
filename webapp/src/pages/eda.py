"""Page for EDA"""

import streamlit as st
from PIL import Image

def write():
    data_desc = st.beta_container()
    """Used to write the page in the app.py file"""
    with data_desc:
        st.title("Exploratory Data Analysis")
        st.subheader("""
        `First Dataset` 
        """)
        st.write('The base dataset contains around **25000** tweets with 3 categories: hate speech, offensive language and neither collected by [Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber(2017)](https://data.world/thomasrdavidson/hate-speech-and-offensive-language).')

        st.image(Image.open('visualization/word_venn.png'), width = 400)
        st.text('')

        st.subheader("""
        `Second Dataset`
        """)
        st.write('We add extract hate speech tweets from [Kaggle](https://www.kaggle.com/dv1453/twitter-sentiment-analysis-analytics-vidya?select=train_E6oV3lV.csv) provided by [Analytics Vidhya](https://datahack.analyticsvidhya.com/contest/practice-problem-twitter-sentiment-analysis/#LeaderBoard).  **2177** tweets of hate speech are added to enrich the number of hate speech tweets in the first dataset after screening some of the hate speech manually.')

        st.text('')

        st.subheader("""
        `Third Dataset`
        """)
        st.write('This dataset is one of the dataset collected by [Jing Qian, Anna Bethke, Yinyin Liu, Elizabeth Belding, William Yang Wang(2019)](https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech). We select **7363** post which is part of the dataset where hate_speech_idx is either 1 or 2.')

        st.text('')

        st.subheader("""
        `Data Distribution in Total`
        """)
        st.image(Image.open('visualization/plot.png'), width = 400)
        