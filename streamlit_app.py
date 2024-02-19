#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import numpy as np

#######################
# Page configuration
st.set_page_config(
    page_title="Recruitment Initial Screening System (RISS)",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="collapsed")

alt.themes.enable("dark")


#######################
# Dashboard Main Panel
st.markdown("## Recruitment Initial Screening System (RISS)")
col = st.columns((1.5, 4.5, 2), gap='medium')

with col[0]:
    
    st.markdown('#### Upload Resume')
    file_path = st.text_input('Resume', 'Enter the file path:')
    # st.write("The current resume is", file_path)
    st.markdown("###### .txt, .docx, .pdf, .zip")
    # if file_path:
    #     try:
    #         with open(file_path, "r") as file:
    #             content = file.read()
    #         st.write(f"Content of the file at '{file_path}':")
    #         st.write(content)
    #     except FileNotFoundError:
    #         # st.error(f"File not found at '{file_path}'")
    #         pass

    file_container = st.container()
    with file_container:
        st.markdown("### Candidates:")
        st.markdown("""
                    Candidate 1 - Test Name1\n
                    Candidate 2 - Test Name2\n
                    Candidate 3 - Sample Name
                    """)


with col[1]:
    with st.container():
        st.markdown("#### Criteria")
        st.checkbox("experience")
        st.checkbox("Academics")
        st.checkbox("Skills")
        st.checkbox("Soft Skills")
        st.checkbox("Flexibility")

        btn = st.download_button(
      label="Process",
      data="byte_im",
      file_name="imagename.png",
      mime="image/jpeg",
      )

        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))

with col[2]:
    st.markdown('#### ')

