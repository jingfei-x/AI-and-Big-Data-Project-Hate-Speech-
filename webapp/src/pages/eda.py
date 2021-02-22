"""Page for EDA"""

import streamlit as st
from PIL import Image

def write():
    data_desc = st.beta_container()
    """Used to write the page in the app.py file"""
    with data_desc:
        st.title("Exploratory Data Analysis")
        st.subheader("""
        The `Dataset1_labeled_data.csv` file has **24,783 rows** where **5.7%** of the tweets were labeled as "Hate Speech".
        """)

        st.image(Image.open('visualization/word_venn.png'), width = 400)
        st.text('')
