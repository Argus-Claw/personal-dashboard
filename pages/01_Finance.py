import streamlit as st
import yfinance as yf
import pandas as pd
import re
from datetime import datetime, timedelta
from functools import lru_cache

st.set_page_config(page_title="Finance", page_icon="📈")

st.title("📈 Finance Tracker")

# Cache API calls for 5 minutes to avoid rate limits
@st.cache_data(ttl=300)
def get_stock_data(ticker, period="6mo"):
    """Fetch stock data with error handling and caching"""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        
        if hist.empty:
            return None, "No data available"
        
        return hist, None
    except Exception as e:
        return None, f"Error fetching data: {str(e)}"

@st.cache_data(ttl=300)
def get_stock_info(ticker):
    """Fetch stock info with fallback"""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # Validate we got useful data
        if not info or ('currentPrice' not in info and 'regularMarketPrice' not in info):
            return None, "No price data available"
        
        price = info.get('currentPrice', info.get('regularMarketPrice', 0))
        prev_close = info.get('previousClose', 0)
        
        return {
            'price': price,
            'prev_close': prev_close,
            'change_pct': ((price - prev_close) / prev_close * 100) if prev_close else 0
        }, None
        
    except Exception as e:
        return None, f"Error: {str(e)}"

def validate_ticker(ticker):
    """Validate stock ticker symbol"""
    if not ticker:
        return False, "Ticker cannot be empty"
    
    # Tickers are typically 1-5 uppercase letters/numbers
    if not re.match(r'^[A-Z0-9]{1,5}$', ticker.upper()):
        return False, "Invalid ticker format (1-5 uppercase letters/numbers only)"
    
    return True, ticker.upper()

# Watchlist
st.subheader("Watchlist")

# HOOD
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.write("**Robinhood (HOOD)**")
    
with col2:
    with st.spinner("Loading..."):
        info, error = get_stock_info("HOOD")
        
        if error:
            st.warning(f"⚠️ {error}")
            st.metric("Price", "Unavailable", "—")
        else:
            st.metric("Price", f"${info['price']:.2f}", 
                     f"{info['change_pct']:+.1f}%")

with col3:
    st.metric("Position", "-34% YTD", "📉", delta_color="off")

# Chart
st.markdown("---")
st.subheader("HOOD - 6 Month Chart")

with st.spinner("Loading chart..."):
    data, error = get_stock_data("HOOD")
    
    if error:
        st.error(f"❌ {error}")
        st.info("Chart temporarily unavailable. Try again later.")
    elif data is not None:
        st.line_chart(data['Close'])
    else:
        st.warning("No chart data available")

# Add ticker form
st.markdown("---")
st.subheader("Add Ticker")

with st.form("add_ticker"):
    ticker = st.text_input("Ticker Symbol", placeholder="AAPL", max_chars=5)
    submitted = st.form_submit_button("Add to Watchlist")
    
    if submitted:
        if not ticker:
            st.error("Please enter a ticker symbol")
        else:
            is_valid, result = validate_ticker(ticker)
            if is_valid:
                # Verify ticker exists via yfinance
                with st.spinner("Verifying ticker..."):
                    try:
                        test = yf.Ticker(result)
                        info = test.info
                        if 'symbol' in info or 'shortName' in info:
                            st.success(f"✅ Added {result} to watchlist")
                        else:
                            st.error(f"❌ Ticker {result} not found")
                    except Exception as e:
                        st.error(f"❌ Could not verify ticker {result}: {str(e)[:100]}")
            else:
                st.error(result)
