import streamlit as st
import matplotlib.pyplot as plt
import requests
import pandas as pd

from tools import get_price, get_news
from agents import run_agent
st.autorefresh(interval=5000)  # refresh every 5 seconds

st.set_page_config(page_title="Crypto AI Dashboard", layout="wide")

st.title("🚀 Crypto AI Intelligence Dashboard")

# =========================
# SIDEBAR
# =========================
coin = st.sidebar.selectbox(
    "Select Coin",
    ["bitcoin", "ethereum", "solana", "binancecoin", "ripple"]
)

st.sidebar.write("AI analyzes market using multi-agent system")

# =========================
# PRICE + NEWS
# =========================
price = get_price(coin)
news = get_news()

st.subheader(f"📊 {coin.upper()} Live Data")
if price is None:
    st.error("Price not available")
else:
    st.metric("Current Price (USD)", f"${price}")

# DEBUG (optional)
st.write("DEBUG PRICE:", price)

# =========================
# CHART DATA (FIXED PROPERLY)
# =========================
import plotly.graph_objects as go

url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
params = {"vs_currency": "usd", "days": 1}

data = requests.get(url, params=params).json()

prices = data.get("prices", [])

if prices:
    df = pd.DataFrame(prices, columns=["time", "price"])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["time"],
        y=df["price"],
        mode="lines",
        name="Price"
    ))

    fig.update_layout(
        title=f"{coin.upper()} Live Price Chart",
        xaxis_title="Time",
        yaxis_title="Price (USD)",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No chart data available")
# =========================
# AI AGENTS
# =========================
st.subheader("🧠 AI Market Analysis")

market = run_agent("Market Analyst", "Analyze price trend", price)
news_a = run_agent("News Analyst", "Analyze crypto news impact", news)
sentiment = run_agent("Sentiment Analyst", "Detect market sentiment", news)

final_input = f"""
Coin: {coin}
Price: {price}

Market: {market}
News: {news_a}
Sentiment: {sentiment}
"""

decision = run_agent(
    "Senior Crypto Strategist",
    "Give BUY/SELL/HOLD with confidence score",
    final_input
)

st.subheader("📢 Final AI Decision")
st.write(decision)

# =========================
# NEWS
# =========================
st.subheader("📰 Latest Crypto News")
st.write(news)