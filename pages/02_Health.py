import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Health", page_icon="💪")

st.title("💪 Health Data")

# Whoop Integration Placeholder
st.info("🔗 *Integrate with Whoop API for automatic sync*")

st.markdown("---")

# Manual entry
col1, col2 = st.columns(2)

with col1:
    st.subheader("Today's Metrics")
    
    recovery = st.slider("Recovery Score", 0, 100, 75)
    sleep_hours = st.number_input("Sleep (hours)", 0.0, 12.0, 7.0, 0.5)
    hrv = st.number_input("HRV (ms)", 0, 200, 140)
    rhr = st.number_input("RHR (bpm)", 30, 100, 55)
    
    if st.button("Log Entry"):
        st.success(f"Logged: {recovery}% recovery, {sleep_hours}h sleep")

with col2:
    st.subheader("This Week")
    
    # Placeholder weekly data
    st.metric("Avg Recovery", "74%", "+2%")
    st.metric("Avg Sleep", "7h 12m", "+15m")
    st.metric("Workouts", "4", "+1")
    st.metric("Strain", "12.4", "-0.8")

st.markdown("---")

# Trends
st.subheader("Weekly Trends")

# Placeholder chart data
import pandas as pd
import numpy as np

days = [(datetime.now() - timedelta(days=i)).strftime('%a') for i in range(6, -1, -1)]
data = pd.DataFrame({
    'Recovery': np.random.randint(65, 90, 7),
    'Sleep': np.random.uniform(6.5, 8.0, 7),
}, index=days)

st.line_chart(data)

# Weight tracking
st.markdown("---")
st.subheader("Weight Log")

with st.form("weight_entry"):
    weight = st.number_input("Weight (lbs)", 100.0, 300.0, 185.0, 0.1)
    note = st.text_input("Note (optional)")
    submitted = st.form_submit_button("Log Weight")
    if submitted:
        st.success(f"Logged: {weight} lbs")
