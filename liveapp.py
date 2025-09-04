import yfinance as yf
import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Set page config
st.set_page_config(page_title="Live Stock Price Viewer", layout="centered")
st.title("📈 Live Stock Price Viewer")

# Auto-refresh every 10 seconds
st_autorefresh(interval=10 * 1000, key="price_refresh")

# User input ticker symbol
ticker_symbol = st.text_input("Enter Stock Ticker (e.g., AAPL, MSFT, TSLA):", "AAPL")

if ticker_symbol:
    try:
        stock = yf.Ticker(ticker_symbol)
        data_today = stock.history(period="1d")

        if not data_today.empty:
            current_price = data_today["Close"].iloc[-1]
            st.metric(label=f"{ticker_symbol} Current Price", value=f"${current_price:.2f}")
        else:
            st.warning("⚠️ No data found for this symbol.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
