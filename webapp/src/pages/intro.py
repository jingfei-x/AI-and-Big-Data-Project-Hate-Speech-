"""Page for Business Problem"""

import streamlit as st
from PIL import Image
def write():
    # creating page sections
    site_header = st.beta_container()

    with site_header:
        st.title('Twitter Hate Speech Detection')
        st.write("""
        This project aims to analyze how could AI **optimize the content moderation processes** for business and **reduce harmful effects** on human moderators [(reference)](https://imagga.com/blog/how-to-handle-content-moderation-with-the-human-factor-in-mind/)
        """)
        st.image(Image.open('visualization/hatespeech.jpeg'), width = 600)