
import streamlit as st
import pandas as pd
import datetime
import random
import time

# --- STYLING STREAMLIT INJECTION BY THE 60-30-10 RULE ---
st.set_page_config(page_title="TATA MOTORS — Inside Radar Terminal", page_icon="📊", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0d1117; color: #f0f6fc; font-family: 'Inter', sans-serif; }
    .fintech-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 15px; margin-bottom: 10px; }
    .ledger-card { background: #1c2128; border: 1px solid #444c56; border-radius: 10px; padding: 10px; text-align: center; }
    .brand-title { font-size: 36px; font-weight: 800; color: #ffffff; margin-bottom: 0px; }
    .brand-subtitle { color: #1f88e5; font-weight: 600; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# State
if 'tata_live_cmp' not in st.session_state: st.session_state.tata_live_cmp = 945.50
flux = random.uniform(-2.20, 2.20)
st.session_state.tata_live_cmp += flux
cmp = st.session_state.tata_live_cmp

# Header
st.markdown('<p class="brand-title">TATA MOTORS LIMITED</p>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtitle">/ TATAMOTORS (NSE)</p>', unsafe_allow_html=True)

# Tabs
tab1, tab2 = st.tabs(["🦅 HOME OVERVIEW", "📊 ANALYTICAL LEDGER"])

with tab1:
    # 2x2 Matrix (Compact)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='fintech-card'>Price: ₹{cmp:.2f}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='fintech-card'>P/E Ratio: 15.2</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='fintech-card'>Market Cap: 3.3T</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='fintech-card'>Variance: {flux:.2f} INR</div>", unsafe_allow_html=True)

    # Peer Comparison (New)
    st.markdown("### 📊 Peer Comparison")
    peer_df = pd.DataFrame({
        "Company": ["Tata Motors", "Mahindra", "Maruti"],
        "P/E": [15.2, 22.1, 28.5],
        "Price": [1000, 2500, 12000]
    })
    st.dataframe(peer_df, use_container_width=True)

    # News (Bullet Points - Clean)
    st.markdown("### 📡 Latest Updates")
    st.markdown("• **Q1 FY26 Results:** Revenue at ₹ 104,407 Cr.")
    st.markdown("• **New Launches:** Tiago & Tiago EV platforms released.")
    st.markdown("• **Logistics:** Ace Gold+ XL truck introduced.")
    st.markdown("• **Sustainability:** HPCL Circular Economy JV formed.")

with tab2:
    st.write("Audited financial ledgers are available in the repository records.")

# Refresh
time.sleep(2)
st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

# --- GLOBAL REFRESH CONTROLLER SCRIPT SYNC ---
time.sleep(2)
st.rerun()
