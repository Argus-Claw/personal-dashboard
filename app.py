import streamlit as st
import pandas as pd
import numpy as np
import hashlib
import time
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

# Password protection with rate limiting and hashing
def check_password():
    # Rate limiting setup
    if "failed_attempts" not in st.session_state:
        st.session_state["failed_attempts"] = 0
        st.session_state["lockout_until"] = 0
    
    # Check lockout
    if time.time() < st.session_state["lockout_until"]:
        st.error("🔒 Too many failed attempts. Try again in 5 minutes.")
        st.stop()
    
    def password_entered():
        entered = st.session_state["password"]
        entered_hash = hashlib.sha256(entered.encode()).hexdigest()
        
        # Get hashed password from secrets
        correct_hash = st.secrets.get("APP_PASSWORD_HASH")
        
        if correct_hash is None:
            st.error("⚠️ APP_PASSWORD_HASH not configured in secrets!")
            st.session_state["password_correct"] = False
            return
        
        if entered_hash == correct_hash:
            st.session_state["password_correct"] = True
            st.session_state["failed_attempts"] = 0
            st.session_state["login_time"] = time.time()
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False
            st.session_state["failed_attempts"] += 1
            
            # Lockout after 5 failed attempts
            if st.session_state["failed_attempts"] >= 5:
                st.session_state["lockout_until"] = time.time() + 300  # 5 min
    
    # Session timeout (30 minutes)
    if "login_time" in st.session_state:
        if time.time() - st.session_state["login_time"] > 1800:
            st.session_state.clear()
            st.rerun()
    
    if "password_correct" not in st.session_state:
        st.text_input("Enter password", type="password", 
                     on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter password", type="password", 
                     on_change=password_entered, key="password")
        attempts = st.session_state.get("failed_attempts", 0)
        st.error(f"😕 Password incorrect ({attempts}/5)")
        return False
    else:
        return True

# Enable auth before deployment
if not check_password():
    st.stop()

# Header
st.title("👁️ Personal Dashboard")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M %Z')}")
st.markdown("---")

# Layout: 3 columns for main widgets
col1, col2, col3 = st.columns(3)

# Column 1: Whoop Health Summary
with col1:
    st.subheader("💪 Recovery")
    
    with st.container():
        st.metric("Recovery Score", "78%", "+5%")
        st.metric("Sleep", "7h 23m", "+32m")
        st.metric("HRV", "142 ms", "+8 ms")
        st.info("📊 *Connect Whoop API for live data*")

# Column 2: Stock Portfolio
with col2:
    st.subheader("📈 Portfolio")
    
    st.metric("HOOD", "$18.42", "-2.3%", delta_color="inverse")
    st.metric("YTD", "-34%", "📉", delta_color="off")
    st.caption("*Add more tickers in config*")

# Column 3: Weather & Day
with col3:
    st.subheader("🌤️ Today")
    
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

# Password hash generator helper (commented out)
# Uncomment and run locally to generate hash for secrets
# import hashlib
# password = "your-secure-password"
# print(hashlib.sha256(password.encode()).hexdigest())
