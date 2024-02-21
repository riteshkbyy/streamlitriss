#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from io import StringIO
from docx import Document
import PyPDF2
import zipfile
#######################
# Page configuration
st.set_page_config(
    page_title="Recruitment Initial Screening System (RISS)",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="collapsed")

alt.themes.enable("dark")

# def file_selector(folder_path='C:\\'):
#     filenames = os.listdir(folder_path)
#     selected_filename = st.selectbox('Select a file', filenames)
#     return os.path.join(folder_path, selected_filename)

def process_uploaded_file(uploaded_file):
    if uploaded_file.name[-4:] == '.zip':
        with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
            zip_ref.extractall('data/')
            if uploaded_file.name[-4:]=='.txt':
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                string_data = stringio.read()
                st.write(count,string_data[0:100])
                count+=1
            elif uploaded_file.name[-5:]=='.docx':
                doc = Document(uploaded_file)
                txt_content = ""
                for paragraph in doc.paragraphs:
                    txt_content += paragraph.text + "\n"
                try:
                    st.write(count,txt_content[0:100])
                except IndexError:
                    st.write(count,txt_content)
                count+=1
            elif uploaded_file.name[-4:]=='.pdf':
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                txt_content = ""
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    txt_content += page.extract_text()
                st.write(count,txt_content[0:100])
                count+=1


#######################
# Dashboard Main Panel
st.markdown("## Recruitment Initial Screening System (RISS)")
col = st.columns((1.5, 4.5, 2), gap='medium')

with col[0]:
    st.write("#### Resumes")
    uploaded_files = st.file_uploader(label="", type=[".docx",".doc",".pdf",".txt",".zip"], accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
    # st.markdown(uploaded_file)
    count = 1
    for uploaded_file in uploaded_files:
        if uploaded_file.name[-4:] == '.zip':
            with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
                for name in zip_ref.namelist():
                    data = zip_ref.read(name)
                    st.write(count, name, repr(data[:100]))
                    count+=1
        if uploaded_file.name[-4:]=='.txt':
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            string_data = stringio.read()
            st.write(count,string_data[0:100])
            count+=1
        elif uploaded_file.name[-5:]=='.docx':
            doc = Document(uploaded_file)
            txt_content = ""
            for paragraph in doc.paragraphs:
                txt_content += paragraph.text + "\n"
            try:
                st.write(count,txt_content[0:100])
            except IndexError:
                st.write(count,txt_content)
            count+=1
        elif uploaded_file.name[-4:]=='.pdf':
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            txt_content = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                txt_content += page.extract_text()
            st.write(count,txt_content[0:100])
            count+=1

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

                
    # with st.expander('About', expanded=True):
    #     st.write('''
    #         - Data: [U.S. Census Bureau](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html).
    #         - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
    #         - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
    #         ''')
