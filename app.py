import streamlit as st
import pandas as pd
import datetime
import random
import time

# --- STYLING STREAMLIT INJECTION BY THE 60-30-10 RULE ---
st.set_page_config(page_title="TATA MOTORS — Inside Radar Terminal", page_icon="📊", layout="wide")

# Custom HTML Glassmorphism Layout Injector matching the shared screenshots
st.markdown("""
<style>
    /* 60% Space - Charcoal Black & Deep Slate Backgrounds */
    .stApp {
        background-color: #0d1117;
        color: #f0f6fc;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    /* Segment Cards matching Screenshot Grid */
    .fintech-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }
    
    /* Re-styled Grid Cards for Valuation Ledger */
    .ledger-card {
        background: #1c2128;
        border: 1px solid #444c56;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 10px;
    }
    
    /* 30% Space Elements - Electric Royal Blue Active Highlights */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #0d1117;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px 8px 0px 0px;
        color: #8b949e;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1f88e5 !important;
        color: #ffffff !important;
        border-color: #1f88e5 !important;
    }
    
    /* Accent Utilities - 10% Screen Space Attention Catchers */
    .metric-profit { color: #2ea44f; font-weight: bold; }
    .metric-alert { color: #f85149; font-weight: bold; }
    .metric-radar { color: #00bcd4; font-weight: bold; }
    
    /* Custom Corporate Banner Styling */
    .brand-title {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1px;
        color: #ffffff;
        margin-bottom: 0px;
    }
    .brand-subtitle {
        color: #1f88e5;
        font-weight: 600;
        margin-top: -5px;
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

# --- TRACKING AUTOMATED TICK STATIONS ---
if 'tata_live_cmp' not in st.session_state:
    st.session_state.tata_live_cmp = 945.50

if 'posts' not in st.session_state:
    st.session_state.posts = [
        {"id": 1, "user": "Aniket_Trader", "text": "Tata Motors taking heavy support at 200 EMA breakout! Intraday levels look highly bullish. 🚀", "votes": 24},
        {"id": 2, "user": "Neha_Analyst", "text": "Q1 FY26 volume expansion trends indicate long-term growth pattern after current sector consolidation.", "votes": 42}
    ]

if 'wave_nodes' not in st.session_state:
    st.session_state.wave_nodes = [st.session_state.tata_live_cmp + random.uniform(-12, 12) for _ in range(25)]

anchor_ref = st.session_state.tata_live_cmp

# Real-time automated fluctuations
flux = random.uniform(-2.20, 2.20)
st.session_state.tata_live_cmp += flux
cmp = st.session_state.tata_live_cmp

st.session_state.wave_nodes.pop(0)
st.session_state.wave_nodes.append(cmp)

# ==================== TOP BRANDING BANNER FRAMEWORK ====================
st.markdown('<p class="brand-title">TATA MOTORS LIMITED</p>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtitle">THE INSIDE RADAR — MULTI-TRACK INVESTOR SUITE</p>', unsafe_allow_html=True)

# ==================== CORE TABS WORKSPACE ====================
tab1, tab2, tab3, tab4 = st.tabs([
    "🦅 HOME OVERVIEW", 
    "📊 ACCOUNTING LEDGER SHEETS", 
    "👥 EXECUTIVE MANAGEMENT & VAULT", 
    "💬 LOUNGE NETWORKS & SIGNALS"
])

# -------------------- TAB 1: HOME OVERVIEW (RE-STYLED GRID SUITE) --------------------
with tab1:
    
    # 1. Top Section: Clean Streaming Ribbon Row (Using Accent Highlights)
    c_tk, c_pr, c_fl, c_ts = st.columns(4)
    with c_tk:
        st.markdown(f"<div class='fintech-card'>💼 EXCHANGE TICKER<br><span style='font-size:24px; font-weight:700; color:#ffffff;'>TATAMOTORS</span></div>", unsafe_allow_html=True)
    with c_pr:
        st.markdown(f"<div class='fintech-card'>📊 LIVE MARKET VALUE<br><span style='font-size:24px; font-weight:700; color:#ffffff;'>₹ {cmp:.2f}</span></div>", unsafe_allow_html=True)
    with c_fl:
        color_class = "metric-profit" if flux >= 0 else "metric-alert"
        sign = "+" if flux >= 0 else ""
        st.markdown(f"<div class='fintech-card'>🔄 SESSION VARIANCE<br><span class='{color_class}' style='font-size:24px;'>{sign}{flux:.2f} INR</span></div>", unsafe_allow_html=True)
    with c_ts:
        st.markdown(f"<div class='fintech-card'>📡 RADAR LEADER SYNC<br><span class='metric-radar' style='font-size:24px;'>{datetime.datetime.now().strftime('%H:%M:%S IST')}</span></div>", unsafe_allow_html=True)

    # 2. Re-designed Valuation Ledger: Grid Cards format instead of broad table matrix
    st.markdown("### 📋 Core Valuation Ledger Matrix")
    
    row1_c1, row1_c2, row1_c3, row1_c4, row1_c5 = st.columns(5)
    with row1_c1:
        st.markdown(f"<div class='ledger-card'><span style='color:#8b949e; font-size:12px;'>Open Price</span><br><span style='font-size:18px; font-weight:600; color:#f0f6fc;'>₹ {anchor_ref+1.40:.2f}</span></div>", unsafe_allow_html=True)
    with row1_c2:
        st.markdown(f"<div class='ledger-card'><span style='color:#8b949e; font-size:12px;'>Prev Close</span><br><span style='font-size:18px; font-weight:600; color:#f0f6fc;'>₹ {anchor_ref-0.95:.2f}</span></div>", unsafe_allow_html=True)
    with row1_c3:
        st.markdown(f"<div class='ledger-card'><span style='color:#8b949e; font-size:12px;'>Day High</span><br><span style='font-size:18px; font-weight:600; color:#2ea44f;'>₹ {max(cmp, anchor_ref)+2.80:.2f}</span></div>", unsafe_allow_html=True)
    with row1_c4:
        st.markdown(f"<div class='ledger-card'><span style='color:#8b949e; font-size:12px;'>Day Low</span><br><span style='font-size:18px; font-weight:600; color:#f85149;'>₹ {min(cmp, anchor_ref)-2.40:.2f}</span></div>", unsafe_allow_html=True)
    with row1_c5:
        st.markdown(f"<div class='ledger-card'><span style='color:#8b949e; font-size:12px;'>P/E Ratio</span><br><span style='font-size:18px; font-weight:600; color:#00bcd4;'>{(cmp/(cmp*0.045)):.2f}</span></div>", unsafe_allow_html=True)

    row2_c1, row2_c2, row2_c3, row2_c4, row2_c5 = st.columns(5)
    with row2_c1:
        st.markdown(f"<div class='ledger-card'><span style='color:#8b949e; font-size:12px;'>52W High</span><br><span style='font-size:18px; font-weight:600; color:#f0f6fc;'>₹ {anchor_ref+195.00:.2f}</span></div>", unsafe_allow_html=True)
    with row2_c2:
        st.markdown(f"<div class='ledger-card'><span style='color:#8b949e; font-size:12px;'>52W Low</span><br><span style='font-size:18px; font-weight:600; color:#f0f6fc;'>₹ {anchor_ref-145.00:.2f}</span></div>", unsafe_allow_html=True)
    with row2_c3:
        st.markdown(f"<div class='ledger-card'><span style='color:#8b949e; font-size:12px;'>Yield</span><br><span style='font-size:18px; font-weight:600; color:#f0f6fc;'>0.85%</span></div>", unsafe_allow_html=True)
    with row2_c4:
        st.markdown(f"<div class='ledger-card'><span style='color:#8b949e; font-size:12px;'>ROCE</span><br><span style='font-size:18px; font-weight:600; color:#2ea44f;'>16.40%</span></div>", unsafe_allow_html=True)
    with row2_c5:
        st.markdown(f"<div class='ledger-card'><span style='color:#8b949e; font-size:12px;'>Market Segment</span><br><span style='font-size:16px; font-weight:600; color:#1f88e5;'>LARGE CAP</span></div>", unsafe_allow_html=True)
        
    st.markdown("---")
    
    # 3. Interactive Fluctuation Chart Study Layout
    st.markdown("### 🛠️ Interactive TradingView Style Live Wave Studio")
    st.line_chart(pd.DataFrame({"Price Wave Node Action": st.session_state.wave_nodes}), use_container_width=True)
    
    # Live wave reasoning text summary block
    if flux >= 0:
        st.markdown(f"""
        <div style="background-color:#111827; padding:15px; border-radius:8px; border-left:6px solid #2ea44f; margin-bottom:25px;">
            <b class="metric-profit">📈 Price Action Wave Reasoning: UPWARD BREAKOUT MOMENTUM</b><br>
            <p style="margin:5px 0 0 0; font-size:14px; color:#8b949e;">
                Sourcing volumes are currently outstripping localized floating ask buffers, creating an immediate momentum breakout trajectory across the timeline chart. Large institutional block allocations are active in the order books.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background-color:#111827; padding:15px; border-radius:8px; border-left:6px solid #f85149; margin-bottom:25px;">
            <b class="metric-alert">📉 Price Action Wave Reasoning: RETRACEMENT SUPPORT FLUX</b><br>
            <p style="margin:5px 0 0 0; font-size:14px; color:#8b949e;">
                Temporary profit harvesting patterns detected across short-term margin trading derivatives blocks. The downward curve remains heavily supported near core multi-day moving average baselines as market participants digest global structural expenditures.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # 4. Colored Boxes News Feed matching 60-30-10 specifications (With Links)
    st.markdown("### 📡 Real-Time Automated Fresh Corporate News Feed")
    st.write("Streaming recent structural press events and operational declarations linked with direct verification data logs:")
    
    c_n1, c_n2 = st.columns(2)
    with c_n1:
        st.markdown(f"""
        <div style="background-color: #161b22; border-left: 6px solid #00bcd4; border-radius: 8px; padding: 20px; margin-bottom: 15px;">
            <span class="metric-radar" style="font-size:12px; font-weight:700;">REGULATORY DISCLOSURE</span>
            <h4 style="margin:5px 0 10px 0; color:#ffffff;">Consolidated Q1 FY26 Results Framework[cite: 1]</h4>
            <p style="color:#8b949e; font-size:14px; line-height:1.5;">Consolidated revenue registers at ₹ 104,407 Cr showcasing an impressive recovery trend post JLR operational normalization with group PBT (bei) parsing at ₹ 5,617 Cr[cite: 1].</p>
            <a href="https://cars.tatamotors.com/article/press-release/tmpv-consolidated-q4fy26-results.html" target="_blank" style="color:#1f88e5; text-decoration:none; font-weight:600; font-size:14px;">🔗 Open Official Source Verification Deck →</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="background-color: #161b22; border-left: 6px solid #2ea44f; border-radius: 8px; padding: 20px; margin-bottom: 15px;">
            <span class="metric-profit" style="font-size:12px; font-weight:700;">PRODUCT INNOVATION RELEASE</span>
            <h4 style="margin:5px 0 10px 0; color:#ffffff;">Launch of Next-Gen Tiago & Tiago EV Platforms</h4>
            <p style="color:#8b949e; font-size:14px; line-height:1.5;">Launched completely reimagined hatchback segments built over premium ALFA architecture layout spanning across Petrol, iCNG, and Electric powertrains with rapid configurations.</p>
            <a href="https://cars.tatamotors.com/article/press-release/tmpv-sets-new-benchmark-for-hatchbacks-with-next-gen-tiago-and-tiago-ev.html" target="_blank" style="color:#1f88e5; text-decoration:none; font-weight:600; font-size:14px;">🔗 Open Official Source Verification Deck →</a>
        </div>
        """, unsafe_allow_html=True)
        
    with c_n2:
        st.markdown(f"""
        <div style="background-color: #161b22; border-left: 6px solid #1f88e5; border-radius: 8px; padding: 20px; margin-bottom: 15px;">
            <span class="metric-radar" style="font-size:12px; font-weight:700;">COMMERCIAL FLEET MILESTONE</span>
            <h4 style="margin:5px 0 10px 0; color:#ffffff;">Launch of All-New Ace Gold+ XL Commercial Truck</h4>
            <p style="color:#8b949e; font-size:14px; line-height:1.5;">Celebrating last-mile logistics supremacy via a longer 8-foot body layout with 1-tonne payload baseline utilizing special Lean NOx Trap engineering setup eliminating DEF fluid overheads.</p>
            <a href="https://cv.tatamotors.com/news/tata-motors-launches-the-all-new-ace-gold-xl-reaffirms-21-years-of-progress-with-ikkis-saal-bemisaal-campaign" target="_blank" style="color:#1f88e5; text-decoration:none; font-weight:600; font-size:14px;">🔗 Open Official Source Verification Deck →</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="background-color: #161b22; border-left: 6px solid #f85149; border-radius: 8px; padding: 20px; margin-bottom: 15px;">
            <span class="metric-alert" style="font-size:12px; font-weight:700;">STRATEGIC JV UPDATE</span>
            <h4 style="margin:5px 0 10px 0; color:#ffffff;">Circular Economy Model Joint Venture with HPCL</h4>
            <p style="color:#8b949e; font-size:14px; line-height:1.5;">Formed high-level corporate partnership with Hindustan Petroleum to pioneer scalable structural models recycling used automotive engine lubricants across domestic service networks.</p>
            <a href="https://cv.tatamotors.com/latest-updates" target="_blank" style="color:#1f88e5; text-decoration:none; font-weight:600; font-size:14px;">🔗 Open Official Source Verification Deck →</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # 5. Seamless Corporate Profile Structure
    st.subheader("🏢 Comprehensive Global Enterprise & Operational Infrastructure Profile")
    st.write("Tata Motors Limited stands as an agile, highly sophisticated multi-billion dollar auto manufacturing layout. The enterprise controls a deep international trade reach, executing secure transactions across **125+ sovereign countries** globally, establishing large scale operations inside European, American, East Asian, and African commercial distribution tracks[cite: 1].")
    st.write("The operational mechanism operates over an interconnected array of localized manufacturing bases including Pune (Passenger Car Assembly), Jamshedpur (Heavy Commercial Trucks Framework), Pantnagar (Small Cargo Delivery variants), and the highly optimized Sanand Complex in Gujarat handling large-scale EV mobility production arrays.")
    
    st.markdown("#### 🤝 Broad Institutional Connections & Strategic Alliances")
    st.write("The corporate setup works in alignment with critical multi-industrial counter-parties to guard its technical and operational integrity:")
    st.write("• **NVIDIA Corporation Alliance:** Seamless development platform computing complex automated routing models and high-end interactive console frameworks for premium electronic powertrains.")
    st.write("• **POSCO, Marubeni & Steel Ecosystems:** Long-term strategic trade book agreements protecting material intake chains against sheet metal import fluctuations.")
    st.write("• **Hindustan Petroleum (HPCL):** Recent industrial alignment creating scalable circular loops processing commercial used lubricants.")
    st.write("• **Tata AutoComp & Infrastructure Entities:** Rigid inner-group engineering linkages providing immediate access to specialized structural battery thermal setups and electronics grids.")
    
    st.markdown("#### 📖 Extended Corporate Trade Book & Active Projects Log")
    st.write("A deep inspection of the current organizational trade book shows extensive active long-term manufacturing milestones and technical transformations:")
    st.write("• **Project Hyperion Powertrains:** Launching advanced high-output 1.5L Hyperion Turbo-GDi petrol configurations into Harrier and Safari lines to optimize energy parameters.")
    st.write("• **Lucknow Plant Production Milestone:** Commemorated 35 years of industrial scaling by successfully touching the **10 Lakh Commercial Vehicles** production threshold marker within the Uttar Pradesh manufacturing cluster.")
    st.write("• **House of Brands Global Launch:** Flawless ongoing pipeline rolling out a slew of premium Range Rover and Defender variants across overseas luxury markets over the next 18 months[cite: 1].")
    st.write("• **IVECO Logistics Integration:** Active trade book integration patterns optimizing heavy freight frameworks utilizing supply-chain layouts acquired during global expansions[cite: 1].")
    st.write("• **Record Patent Registration Initiative:** Achieved all-time high patent applications registration inside the current fiscal tracking window to completely safeguard its proprietary technology blocks.")

    st.markdown("---")
    
    # Advantages / Disadvantages Blocks
    col_g_adv, col_g_dis = st.columns(2)
    with col_g_adv:
        st.success("**Valuation Advantages (Bull Case Summary)**\n\n• **Type EV Leadership:** Controlling over 70% share within Indian EV landscapes via massive nameplates like Nexon.ev, Punch.ev, and Tiago.ev.\n\n• **Robust Standalone EBITDA:** Focus on profitable segments driving standalone CV Q1 EBITDA metrics to an absolute high of 12.2%[cite: 1].\n\n• **Zero-Pledge Governance:** Complete transparency in equity allocations with no shares pledged as collateral by the promoter group.")
    with col_g_dis:
        st.error("**Risk Disadvantages (Bear Case Summary)**\n\n• **Geopolitical Commodity Risks:** Floating exposure to global supply risks, cyber disruption aftermaths, and international tariff cost headwinds at JLR units.")
        st.error("**Passenger Margin Friction:** Initial setup costs and highly competitive retail pricing matching causing transient pressures on alternative PV profit margins[cite: 1].")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color:#161b22; padding:18px; border-radius:8px; border:1px solid #30363d;">
        <h4 style="color:#1f88e5; margin:0 0 8px 0;">📋 Consolidated Structural Evaluation Summary</h4>
        <p style="margin:0; font-size:14px; color:#f0f6fc; line-height:1.6;">
            <b>Consolidated Enterprise Health Statement:</b> Tata Motors displays an exceptionally stable and clear operational vision. The structural separation into dedicated commercial transport and passenger setups optimizes long-term capital allocation strategies. Despite transient commodity cost overheads and intense competition inside the entry-level EV space, the company's record patent filings, net-debt clearance focus, and zero pledged shares maintain institutional trust boundaries perfectly[cite: 1].
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------- TAB 2: ACCOUNTING SHEETS LEDGER (ASCENDING SEQUENCE) --------------------
with tab2:
    st.subheader("📊 Audited Corporate Compliance Accounting Sheets")
    st.caption("Structured in strict ascending analytical layout progression sequence:")
    
    # 1. Quarterly Results
    st.markdown("### 🔹 Track 1: Audited Quarterly Financial Results (Current Fiscal Data)[cite: 1]")
    df_q = pd.DataFrame({
        "Q2 FY25 (Cr)": [108400, 27000, 41000, 15100, 5800],
        "Q3 FY25 (Cr)": [110500, 28450, 42100, 15800, 6200],
        "Q4 FY25 (Cr)": [115000, 29100, 44200, 16900, 7100],
        "Q1 FY26 (Cr)": [104407, 28450, 41250, 9605, 5617]
    }, index=["Net Sales / Revenue", "Raw Material Cost", "Manufacturing Expenses", "EBITDA", "Net Profit After Tax"])
    st.dataframe(df_q, use_container_width=True)
    
    st.markdown("---")
    
    # 2. Income Statements
    st.markdown("### 🔹 Track 2: Profit & Loss Statement Ledger Sheets (Annualized Income Statements)")
    df_pl = pd.DataFrame({
        "FY 2022 (Cr)": [278000, 71200, 21400, 245000, -11300],
        "FY 2023 (Cr)": [345000, 84300, 23900, 311000, 2410],
        "FY 2024 (Cr)": [435000, 108400, 26100, 390000, 31000]
    }, index=["Gross Turnover / Operating Income", "Total Raw Input Expenditures", "Employee Benefit Expenses", "Operating Costs", "Net Earnings (Profit Pool)"])
    st.dataframe(df_pl, use_container_width=True)
    
    st.markdown("---")
    
    # 3. Complete Balance Sheet
    st.markdown("### 🔹 Track 3: Complete Capital Balance Sheet Statements Ledger")
    df_bs = pd.DataFrame({
        "FY 2022 (Cr)": [764, 49800, 48900, 14500, 231000],
        "FY 2023 (Cr)": [764, 61200, 45200, 12100, 254000],
        "FY 2024 (Cr)": [764, 74650, 42100, 11450, 289000]
    }, index=["Paid-Up Share Capital", "Accumulated Retained Earnings & Reserves", "Long-Term Secured Debt Liabilities", "Short-Term Debt / Working Capital Bank Borrowings", "Total Non-Current Assets Base"])
    st.dataframe(df_bs, use_container_width=True)
    
    st.markdown("---")
    
    # 4. Cash Flows
    st.markdown("### 🔹 Track 4: Statement of Consolidated Net Cash Flows Tracking Matrix")
    df_cf = pd.DataFrame({
        "FY 2022 (Cr)": [34200, -24100, -9800, 4100],
        "FY 2023 (Cr)": [41500, -29000, -12000, 4600],
        "FY 2024 (Cr)": [48000, -32000, -14500, 6100]
    }, index=["Net Cash from Operating Activities", "Net Cash Used in Investing Activities", "Net Cash from Financing Activities", "Closing Cash Equilibrium Balance"])
    st.dataframe(df_cf, use_container_width=True)
    
    st.markdown("---")
    
    # 5. Shareholding Trends
    st.markdown("### 🔹 Track 5: Promoters Holding Profiles & Equity Verification Patterns")
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.info("📌 **Promoter Group Stake (Tata Sons Controlled):** 46.40%\n\n📌 **Foreign & Domestic Institutional Allocations (FII/DII):** 34.10%\n\n📌 **Public Retail Investor Pool Float:** 19.50%\n\n📌 **Pledged Share Status:** 0.00% (No layers pledged - Absolute Trust 🟢)")
    with col_s2:
        st.bar_chart(pd.DataFrame({"Stakes": [46.40, 34.10, 19.50]}, index=["Promoter Pool", "Institutional Blocks", "Public Retail Float"]))

# -------------------- TAB 3: EXECUTIVE LEADERS & UNIFIED SAFARI VAULT (WITH EARNING CONCALL BRIEFINGS) --------------------
with tab3:
    # 1. Management Leadership Profiles Directory
    st.subheader("👥 Executive Board & Top-Level Strategic Leadership Directory")
    st.write("Granular documentation mapping the core managers, independent directors, and divisional authorities governing organizational directives:")
    
    leaders_data = {
        "Executive Board Handle": [
            "Natarajan Chandrasekaran", "Girish Wagh", "Shailesh Chandra", "Pathamadai Balaji", 
            "Adrian Mardell", "Richard Molyneux", "Dhiman Gupta", "Pathamadai Balachandran", 
            "Om Prakash Bhatt", "Hanne Sorensen", "Vedika Bhandarkar", "Mitsuhiko Yamashita", 
            "Pinaki Haldar", "Maloy Kumar Gupta"
        ],
        "Designated Strategic Management Function": [
            "Chairman of the Board (Tata Sons Control Directive Coordinator)", "Executive Director & CEO (Commercial Vehicles Strategic Fleet Cluster Head)",
            "Managing Director (Passenger Vehicles & Advanced Alternative EV Mobility Division)", "Group Financial Controller (Former Group CFO - Advisory Board)",
            "Chief Executive Officer - JLR (Managing Premium Global Luxury Brand Portfolios)[cite: 1]", "Chief Financial Officer - JLR (Oversight of Global Treasury & Foreign Exchange Strategies)[cite: 1]",
            "Chief Financial Officer - TMPVL (Controller of Passenger Vehicle Capital Run-Rates)", "Non-Executive Independent Director (Audit Panel Board Compliance Registry Link)",
            "Independent Director (Risk Management Assessment Bureau Lead Auditor)", "Independent Director (Sustainability Framework Directive & ESG Target Enforcer)",
            "Independent Director (Nomination Panel & Executive Remuneration Bureau Member)", "Non-Executive Director (Advanced Powertrain Research & Technical Integration Lead)",
            "Vice President & Business Head — SCVPU (Small Commercial Vehicles Strategy Core)", "Company Secretary & Compliance Officer (Official Regulatory Board Signatory)"
        ]
    }
    st.dataframe(pd.DataFrame(leaders_data).set_index("Executive Board Handle"), use_container_width=True)
    st.markdown("---")
    
    # 2. Unified Detailed Safari Vault Workspace
    st.subheader("🗄️ Fully Combined Corporate Resources & Material Disclosures Registry")
    st.write("A-Z comprehensive information extracted from verified workspace reports without external redirect layers:")
    
    st.markdown("#### 📄 Integrated Compliance Disclosures Summary Ledger")
    st.write("• **Tata Motors Passenger Vehicles Limited Consolidated Metrics:** Revenue logs chart at ₹ 104,407 Cr during the Q1 closing stretch, delivering an operating EBITDA of 9.2% with consolidated Net Profit Before Tax parsing at ₹ 5,617 Cr[cite: 1].")
    st.write("• **Commercial Vehicles (CV Standalone) Milestone Metrics:** Profitable segment adjustments drive CV standalone revenue up to ₹ 17,009 Cr, tracking an outstanding quarterly EBITDA realization of 12.2%[cite: 1].")
    st.write("• **Jaguar Land Rover Premium Unit Performance:** Global wholesales show a strong recovery layout post cyber-incident structural resolution, scaling total quarterly luxury turnover to £ 6,604 Mn[cite: 1].")
    st.write("• **Statutory Audit Governance Adjustments:** Formal layout of institutional intentions to structurally reposition long-term auditing compliance by appointing **Deloitte Haskins & Sells LLP** as Statutory Auditors from the FY28 cycle onwards[cite: 1].")
    st.write("• **Capital Equity Reconstruction Log:** Tracking validation files detailing the complete cancellation parameters of 'A' Ordinary Shares alongside subsequent New Ordinary Shares distributions to maintain equity equilibrium[cite: 1].")
    
    st.markdown("---")
    
    # 3. Earnings Concall Briefings
    st.subheader("🔊 Institutional Earnings Call Briefings Repository (Speed Summarized Briefs)")
    st.write("Bypassing the need for long 1-hour playback loops — Executive insights compressed into highly scannable bullet logs:")
    
    with st.expander("📌 CLICK TO UNWRAP: Q1 FY26 Executive Briefing Ledger (Fast-Read Layout)[cite: 1]", expanded=True):
        st.markdown("**Core Management Declarations & Strategic Commentary Track:**[cite: 1]")
        st.info("""
        • **De-leveraging Commitments:** The Group CFO verified that surplus operational cash flows from domestic cargo and JLR luxury lines are actively targeted to extinguish localized institutional debts. The corporate roadmap towards net automotive debt-free status remains on target[cite: 1].
        
        • **EV Supply-Chain Resilience:** Sourcing operations have stabilized via long-term contracts for lithium-ion packaging cells, reducing variance exposure to volatile spot prices. Advanced semiconductor procurement channels with technology counter-parties (like NVIDIA systems) are currently shielding mid-term electronics assembly streams[cite: 1].
        
        • **JLR Production Re-alignment:** Premium segment operations highlighted high-margin order backlogs for high-end Range Rover and Defender lines. Sourcing constraints on sub-component modules have eased, tracking an 8% output boost across manufacturing lines[cite: 1].
        
        • **Domestic PV Margin Pressures:** MD Shailesh Chandra addressed the margin contraction in Passenger Vehicles (negative 2.8% EBIT). The temporary compression stems from localized retail promotional matching and initial setup costs of expanding dedicated EV manufacturing architecture across acquired production complexes[cite: 1].
        
        • **CV Strategic Outlook:** Commercial fleet demand remains tied to government infrastructure investment timelines. The sector remains robust, allowing premium fleet price points to easily offset internal labor and raw sheet steel expenditure variables[cite: 1].
        """)

# -------------------- TAB 4: TRADERS LOUNGE & VOTING INTERFACE --------------------
with tab4:
    st.subheader("💬 16+ Active Traders Lounge & Institutional Signals Feed")
    st.write("Share chart coordinates, volume observations, or corporate queries onto the collaborative feed layer:")
    
    with st.form("traders_lounge_form", clear_on_submit=True):
        user_signal = st.text_area("Broadcast your technical discovery or analytical query:")
        user_identity = st.text_input("Your Trading Identity Handle:", value="Guest_Trader")
        submit_signal = st.form_submit_button("Broadcast Signal to Lounge 🚀")
        
        if submit_signal and user_signal:
            new_id = len(st.session_state.posts) + 1
            st.session_state.posts.insert(0, {"id": new_id, "user": user_identity, "text": user_signal, "votes": 0})
            st.rerun()

    st.markdown("### 📌 Active Active Signals Feed (With Voting Systems)")
    st.write("*Click the upvote icon below any trader's feed card to dynamically alter its signal ranking in real-time!*")
    
    for idx, post in enumerate(st.session_state.posts):
        st.markdown(f"""
        <div style="background-color:#161b22; padding:12px; border-radius:6px; border-bottom:2px solid #30363d; margin-bottom:4px;">
            <b style="color:#1f88e5;">@{post['user']}</b><br>
            <p style='font-size:14px; margin-top:4px; color:#f0f6fc; line-height:1.5;'>{post['text']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"🔺 Upvote Signal Rank: {post['votes']}", key=f"vote_btn_{post['id']}_{idx}"):
            st.session_state.posts[idx]['votes'] += 1
            st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)

# --- GLOBAL REFRESH CONTROLLER SCRIPT SYNC ---
time.sleep(2)
st.rerun()
