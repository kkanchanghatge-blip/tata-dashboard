import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
import time

# --- SETUP ---
st.set_page_config(page_title="TATA MOTORS CV — Inside Radar Terminal", layout="wide")
TICKER = "TATAMOTORS.NS"

# --- HELPER: REAL DATA FETCHING ---
@st.cache_data(ttl=60)
def get_live_data():
    stock = yf.Ticker(TICKER)
    info = stock.info
    hist = stock.history(period="1d")
    return info, hist

info, hist = get_live_data()
current_price = hist['Close'].iloc[-1]
prev_close = info.get('previousClose', 0)
flux = current_price - prev_close

# --- HEADER & RADAR ---
st.title("🚛 TATA MOTORS CV — LIVE RADAR TERMINAL")
col_h1, col_h2 = st.columns([3, 1])
col_h1.write(f"**Last Sync:** {datetime.datetime.now().strftime('%H:%M:%S IST')}")
col_h2.metric("LIVE PRICE", f"₹{current_price:.2f}", f"{flux:.2f}")

# --- RADAR & NEWS FEED ---
st.markdown("### 📡 Live Radar & Market Analysis")
col1, col2 = st.columns([1, 1])
with col1:
    st.line_chart(hist['Close'])
    st.markdown("### 🤖 AI Market Sentiment")
    st.info("Tata Motors CV continues to dominate the HCV segment. Current indicators suggest holding until the ₹384 resistance is cleared.")
with col2:
    st.markdown("### 📰 Recent News Feed")
    st.write("• **Q1 FY26 Results:** Consolidated revenue at ₹104,407 Cr.")
    st.write("• **Production:** Lucknow plant crossed 10 Lakh unit milestone.")
    st.write("• **Strategic:** Circular economy JV formed with HPCL.")

# --- VALUATION LEDGER ---
st.markdown("---")
st.subheader("📋 Core Valuation Ledger Matrix")
l_cols = st.columns(5)
l_cols[0].metric("Open", f"₹{info.get('open', 0):.2f}")
l_cols[1].metric("Prev Close", f"₹{prev_close:.2f}")
l_cols[2].metric("Day High", f"₹{info.get('dayHigh', 0):.2f}")
l_cols[3].metric("Day Low", f"₹{info.get('dayLow', 0):.2f}")
l_cols[4].metric("Mkt Cap", f"{info.get('marketCap', 0)/1e12:.2f}T")

# --- STRENGTHS & WEAKNESSES ---
st.markdown("---")
c_s, c_w = st.columns(2)
c_s.success("**Strengths:** 35.7% CV market share, Zero-Pledge Governance, High EBITDA.")
c_w.error("**Weakness:** Geopolitical commodity risks & competitive PV margins.")

# --- VOTING ---
st.markdown("---")
if 'poll' not in st.session_state: st.session_state.poll = {"Buy": 0, "Hold": 0, "Sell": 0}
st.subheader("🗳️ Daily Live Trader Poll")
p1, p2, p3 = st.columns(3)
if p1.button("👍 Buy"): st.session_state.poll["Buy"] += 1
if p2.button("✋ Hold"): st.session_state.poll["Hold"] += 1
if p3.button("👎 Sell"): st.session_state.poll["Sell"] += 1
st.bar_chart(pd.DataFrame(st.session_state.poll, index=["Votes"]).T)

# --- AUTO REFRESH ---
time.sleep(10)
st.rerun()
# Triggering update
