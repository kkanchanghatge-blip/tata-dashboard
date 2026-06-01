import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

st.set_page_config(page_title="TATA MOTORS CV — Radar", layout="wide")

# Data fetch function with a simple error handling
def get_data():
    try:
        stock = yf.Ticker("TATAMOTORS.NS")
        # Try fetching info, if it fails, return basic data
        info = stock.info
        hist = stock.history(period="1d")
        return info, hist
    except Exception as e:
        st.error(f"Data fetch error: {e}")
        return None, None

st.title("🚛 TATA MOTORS CV — LIVE RADAR")

info, hist = get_data()

if info and not hist.empty:
    price = hist['Close'].iloc[-1]
    st.metric("LIVE PRICE", f"₹{price:.2f}")
    
    st.subheader("📋 Core Valuation")
    cols = st.columns(5)
    cols[0].metric("Open", f"₹{info.get('open', 0):.2f}")
    cols[1].metric("Prev Close", f"₹{info.get('previousClose', 0):.2f}")
    cols[2].metric("Day High", f"₹{info.get('dayHigh', 0):.2f}")
    cols[3].metric("Day Low", f"₹{info.get('dayLow', 0):.2f}")
    cols[4].metric("Mkt Cap", f"{info.get('marketCap', 0)/1e12:.2f}T")
else:
    st.warning("Yahoo Finance data temporary unavailable. Please refresh or check later.")
