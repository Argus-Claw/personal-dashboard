import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analytics", page_icon="📈")

st.title("📈 Analytics Dashboard")

# Sample analytics
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 25, 15, 30]
})

fig = px.bar(data, x='Category', y='Value', title='Sample Chart')
st.plotly_chart(fig, use_container_width=True)
