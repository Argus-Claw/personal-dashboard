import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data", page_icon="📋")

st.title("📋 Data Explorer")

uploaded_file = st.file_uploader("Upload CSV", type=['csv'])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    
    st.download_button(
        label="Download as Excel",
        data=df.to_csv(index=False),
        file_name='data.csv',
        mime='text/csv'
    )
