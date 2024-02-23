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
# import win32com.client
import pythoncom

pythoncom.CoInitialize()
#######################
# Page configuration
st.set_page_config(
    page_title="Recruitment Initial Screening System (RISS)",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="collapsed")

alt.themes.enable("dark")

fileslist = []
def process_uploaded_file(uploaded_file):
    if uploaded_file.name[-4:] == '.zip':
        with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
            zip_ref.extractall('data/')
            files = zip_ref.filelist
            return(files)           
def parsetxt(file):
    stringio = StringIO(file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(count,file.name)
    with open("data/"+str(file.name)+'.txt', 'w') as f:
        f.write(string_data)
def parsedocx(file):
    doc = Document(file)
    txt_content = ""
    for paragraph in doc.paragraphs:
        txt_content += paragraph.text + "\n"
    try:
        st.write(count,file.name)
        with open("data/"+str(file.name)+'.txt', 'w') as f:
            f.write(txt_content)
    except IndexError:
        st.write(count,file.name)
        with open("data/"+str(file.name)+'.txt', 'w') as f:
            f.write(txt_content)
def parsepdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    txt_content = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        txt_content += page.extract_text()
    st.write(count,file.name)
    with open("data/"+str(file.name)+'.txt', 'w') as f:
        f.write(txt_content)
def parsedoc(file):
    st.write(count,file.name)
    with open('data/'+file.name, 'wb') as destination_file:
    # Iterate through chunks and write them to the destination file
        for chunk in file.chunks():
            destination_file.write(chunk)
    destination_file.close()

    # word = win32com.client.Dispatch("Word.Application")
    # word.visible = False
    # wb = word.Documents.Open('data/'+file.name)
    # doc = word.ActiveDocument
    # st.write(doc.Range().Text)

#######################
# Dashboard Main Panel
st.markdown("## Recruitment Initial Screening System (RISS)")
col = st.columns((1.5, 4.5, 2), gap='medium')
count = ''
with col[0]:
    # st.markdown("Requirements")
    uploaded_requirements = st.file_uploader(label="Requirements", type=[".docx",".doc",".pdf",".txt"], accept_multiple_files=False, key="requirements", help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
    if uploaded_requirements:
        if uploaded_requirements.name[-4:]=='.txt':
            parsetxt(uploaded_requirements)
        elif uploaded_requirements.name[-5:]=='.docx':
            parsedocx(uploaded_requirements)
        elif uploaded_requirements.name[-4:]=='.pdf':
            parsepdf(uploaded_requirements)
        elif uploaded_requirements [-4:]=='.doc':
            parsedoc(uploaded_requirements)

    # st.write("#### Resumes")
    uploaded_files = st.file_uploader(label="Resumes", type=[".docx",".doc",".pdf",".txt",".zip"], accept_multiple_files=True, key="resumes", help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
    # st.markdown(uploaded_file)
    count = 1
    for uploaded_file in uploaded_files:
        if uploaded_file.name[-4:] == '.zip':
            data = process_uploaded_file(uploaded_file)
            for x in data:
                st.write(count,x.filename)
                count+=1
        if uploaded_file.name[-4:]=='.txt':
            parsetxt(uploaded_file)
            count+=1
        elif uploaded_file.name[-5:]=='.docx':
            parsedocx(uploaded_file)
            count+=1
        elif uploaded_file.name[-4:]=='.pdf':
            parsepdf(uploaded_file)
            count+=1
        elif uploaded_file.name[-4:]=='.doc':
            parsedoc(uploaded_file)
            count+=1

with col[1]:
    st.markdown("#### Criteria")
    with st.container():
        checks = st.columns(4)
        with checks[0]:
            st.checkbox("experience")
            st.checkbox("Flexibility")
        with checks[1]:
            st.checkbox("Academics")
        with checks[2]:
            st.checkbox("Skills")
        with checks[3]:
            st.checkbox("Soft Skills")
        
    btn = st.download_button(
      label="Process",
      data="byte_im",
      file_name="imagename.png",
      mime="image/jpeg",
      )

        # You can call any Streamlit command, including custom components:
    array = np.random.randint(1,10, size = (10,5))
    df = pd.DataFrame(array, columns=("col %d" % i for i in range(5)))
    df.insert(0,"Candidates" , ['Resume 1', 'resume 2', 'resume 3', 'resume 4', 'resume 5', 'resume 6', 'resume 7', 'resume 8',' resume 9', 'resume 10'])

    st.table(df)

with col[2]:
    st.markdown('#### ')

                
    # with st.expander('About', expanded=True):
    #     st.write('''
    #         - Data: [U.S. Census Bureau](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html).
    #         - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
    #         - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
    #         ''')
