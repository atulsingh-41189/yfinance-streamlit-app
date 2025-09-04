import yfinance as yf
import streamlit as st

# Auto-refresh every 10 seconds
count = st.experimental_rerun if hasattr(st, "experimental_rerun") else None
st_autorefresh = st.experimental_rerun if hasattr(st, "experimental_rerun") else None

st.set_page_config(page_title="AAPL Stock Viewer", layout="centered")
st.title("📈 AAPL Stock Viewer (Live Updates)")

# Refresh every 10 seconds
st_autorefresh = st.experimental_rerun if hasattr(st, "experimental_rerun") else None
st_autorefresh = st_autorefresh or (lambda: None)

if "refresh_count" not in st.session_state:
    st.session_state.refresh_count = 0

# Yahoo Finance ticker
ticker_symbol = "AAPL"
stock = yf.Ticker(ticker_symbol)

# --- Current Price ---
st.header("🔴 Current Price (Live)")
data_today = stock.history(period="1d")
if not data_today.empty:
    current_price = data_today["Close"].iloc[-1]
    st.metric(label=f"{ticker_symbol} Price", value=f"${current_price:.2f}")
else:
    st.error("No live data available.")

# --- Last 5 Days Data ---
st.header("📊 Last 5 Days History")
data = stock.history(period="5d")

if not data.empty:
    st.dataframe(data)
    st.line_chart(data["Close"])
else:
    st.warning("No data found.")

# Trigger refresh every 10 seconds
st_autorefresh()
