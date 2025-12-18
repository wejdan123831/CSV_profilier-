import sys
import os
import io 
import csv
import streamlit as st
import pandas as pd
import profiling
import render


st.set_page_config(page_title="CSV Profiler", page_icon="📊", layout="wide")

st.title("📊 CSV Data Profiler")
st.write("Analyze your CSV file efficiently and get detailed insights. ")


if 'report' not in st.session_state:
    st.session_state.report = None
if 'df_preview' not in st.session_state:
    st.session_state.df_preview = None


uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
 
    if st.session_state.df_preview is None:
       
        uploaded_file.seek(0)
        st.session_state.df_preview = pd.read_csv(uploaded_file, nrows=100)
    
    
    st.subheader("  Data Preview (First 5 rows)")
    st.dataframe(st.session_state.df_preview.head())

    
    if st.button("🚀 Generate Profile Analysis"):
        with st.spinner("Analyzing your data..."):
            
            uploaded_file.seek(0)
            stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
            reader = csv.DictReader(stringio)
            data = [row for row in reader]
            headers = reader.fieldnames

            
            st.session_state.report = profiling.profile_csv(data, headers)
            st.success("✅ Analysis Complete!")

    if st.session_state.report:
        report = st.session_state.report
        
        st.divider()
        st.subheader("📈 Summary Statistics")
        
   
        col_m1, col_m2 = st.columns(2)
        col_m1.metric("Total Rows", report['rows'])
        col_m2.metric("Total Columns", len(report['columns']))

     
        st.write("#### 📋 Column Details")
        details_data = []
        for col, info in report['columns'].items():
            details_data.append({
                "Column Name": col,
                "Data Type": info.get('type', 'N/A'),
                "Missing Values": info.get('missing', 0)
            })
        st.table(details_data)

      
        st.write("### 📥 Download Reports")
        c1, c2 = st.columns(2)
        with c1:
            json_str = render.generate_json(report, None)
            st.download_button("Download JSON", json_str, "report.json", "application/json")
        with c2:
            md_str = render.generate_md(report, None)
            st.download_button("Download Markdown", md_str, "report.md", "text/markdown")


else:
    st.session_state.report = None
    st.session_state.df_preview = None