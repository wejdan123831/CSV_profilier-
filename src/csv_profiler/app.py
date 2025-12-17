

import sys
import os
from pathlib import Path

import io 
import streamlit as st
import pandas as pd
import profiling
import render

st.set_page_config(page_title="CSV Profiler", page_icon="📊")

st.title(" CSV Data Profiler")
st.write("upload your file ")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
  
    import  csv
    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    reader = csv.DictReader(stringio)
    data = [row for row in reader]
    headers = reader.fieldnames

   
    report = profiling.profile_csv(data, headers)
    
    st.success("✅ now you can dawnload json and Markdown files ")

    
    col1, col2 = st.columns(2)
    with col1:
        st.download_button("📥 Download JSON", render.generate_json(report, None), "report.json")
    with col2:
        st.download_button("📥 Download Markdown", render.generate_md(report, None), "report.md")