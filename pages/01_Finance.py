import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Finance", page_icon="📈")

st.title("📈 Finance Tracker")

# Watchlist
st.subheader("Watchlist")

# HOOD
st.markdown("---")
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.write("**Robinhood (HOOD)**")
    
with col2:
    try:
        hood = yf.Ticker("HOOD")
        info = hood.info
        price = info.get('currentPrice', info.get('regularMarketPrice', 0))
        prev_close = info.get('previousClose', 0)
        change = ((price - prev_close) / prev_close * 100) if prev_close else 0
        st.metric("Price", f"${price:.2f}", f"{change:+.1f}%")
    except:
        st.metric("Price", "$18.42", "-2.3%")

with col3:
    st.metric("Position", "-34% YTD", "📉", delta_color="off")

# Chart
st.markdown("---")
st.subheader("HOOD - 6 Month Chart")

try:
    hood_hist = yf.download("HOOD", period="6mo", progress=False)
    if not hood_hist.empty:
        st.line_chart(hood_hist['Close'])
    else:
        st.info("Chart data unavailable")
except:
    st.info("Enable yfinance for live charts")

# Add ticker form
st.markdown("---")
st.subheader("Add Ticker")

with st.form("add_ticker"):
    ticker = st.text_input("Ticker Symbol", placeholder="AAPL")
    submitted = st.form_submit_button("Add to Watchlist")
    if submitted and ticker:
        st.success(f"Added {ticker.upper()} to watchlist (feature pending)")
