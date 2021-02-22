"""Main module for the streamlit app"""

import streamlit as st
import src.pages.eda
import src.pages.app
import src.pages.intro
import src.pages.model


PAGES = {
    "App": src.pages.app,
    "Business Problem": src.pages.intro,
    "EDA": src.pages.eda,
    "Model": src.pages.model,
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.write()

    with st.spinner(f"Loading {selection} ..."):
        st.sidebar.title("About")
        st.sidebar.info(
            "This app is maintained by TBS Students in BA&AI. \n\n"
            "Check out the project repository [here](https://github.com/jingfei-x/AI-and-Big-Data-Project-Hate-Speech-)"
    )



if __name__ == "__main__":
    main()