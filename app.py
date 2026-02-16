import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests
import json
import os

st.set_page_config(
    page_title="Joe's Personal Dashboard",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Simple password protection (optional)
def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets.get("APP_PASSWORD", "admin"):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect")
        return False
    else:
        return True

# Uncomment to enable auth
# if not check_password():
#     st.stop()

# Header
st.title("👁️ Personal Dashboard")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M %Z')}")
st.markdown("---")

# Layout: 3 columns for main widgets
col1, col2, col3 = st.columns(3)

# Column 1: Whoop Health Summary
with col1:
    st.subheader("💪 Recovery")
    
    # Placeholder - would integrate with Whoop API
    whoop_placeholder = st.container()
    with whoop_placeholder:
        st.metric("Recovery Score", "78%", "+5%")
        st.metric("Sleep", "7h 23m", "+32m")
        st.metric("HRV", "142 ms", "+8 ms")
        st.info("📊 *Connect Whoop API for live data*")

# Column 2: Stock Portfolio
with col2:
    st.subheader("📈 Portfolio")
    
    # HOOD placeholder
    st.metric("HOOD", "$18.42", "-2.3%", delta_color="inverse")
    st.metric("YTD", "-34%", "📉", delta_color="off")
    st.caption("*Add more tickers in config*")

# Column 3: Weather & Day
with col3:
    st.subheader("🌤️ Today")
    
    # Weather placeholder
    st.metric("New York", "42°F", "☁️ Cloudy")
    st.metric("High/Low", "48° / 38°", "")
    
    # Day progress
    now = datetime.now()
    day_start = now.replace(hour=6, minute=0, second=0)
    day_end = now.replace(hour=22, minute=0, second=0)
    day_progress = min(100, max(0, (now - day_start).seconds / (day_end - day_start).seconds * 100))
    
    st.progress(day_progress / 100, text=f"Day progress: {day_progress:.0f}%")

st.markdown("---")

# News Section
st.subheader("📰 Morning Brief")

news_items = [
    ("Finance", "Markets mixed as Fed signals cautious approach", "Reuters"),
    ("Tech", "AI chip demand continues to drive NVIDIA growth", "TechCrunch"),
    ("Supply Chain", "Freight rates stabilize after volatile Q4", "FreightWaves"),
]

for category, headline, source in news_items:
    st.markdown(f"**{category}:** {headline} — *{source}*")

st.markdown("---")

# Quick Actions
st.subheader("⚡ Quick Actions")

action_cols = st.columns(4)
with action_cols[0]:
    if st.button("📝 Log Weight"):
        st.info("Feature: Weight logging")
with action_cols[1]:
    if st.button("💊 Log Meds"):
        st.info("Feature: Medication tracking")
with action_cols[2]:
    if st.button("📓 Daily Note"):
        st.info("Feature: Journal entry")
with action_cols[3]:
    if st.button("🏋️ Log Workout"):
        st.info("Feature: Workout tracking")

st.markdown("---")

# Data visualization placeholder
st.subheader("📊 Weekly Trends")

# Sample data
days = [(datetime.now() - timedelta(days=i)).strftime('%a') for i in range(6, -1, -1)]
sample_recovery = [72, 68, 75, 82, 78, 70, 78]
sample_sleep = [6.5, 7.2, 6.8, 7.5, 7.0, 6.2, 7.4]

chart_data = pd.DataFrame({
    'Day': days,
    'Recovery': sample_recovery,
    'Sleep': sample_sleep
})

st.line_chart(chart_data.set_index('Day'))

st.markdown("---")

# Footer
st.caption("👁️ Argus Dashboard — Built with Streamlit")
