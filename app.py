import streamlit as st
import matplotlib.pyplot as plt
import requests
import pandas as pd

from tools import get_price, get_news
from agents import run_agent

st.set_page_config(page_title="Crypto AI Dashboard", layout="wide")

st.title("Crypto AI Intelligence Dashboard")

# Sidebar
coin = st.sidebar.selectbox(
    "Select Coin",
    ["bitcoin", "ethereum", "solana", "binancecoin", "ripple"]
)

st.sidebar.write("AI analyzes market using multi-agent system")

# =========================
# GET DATA (SAFE)
# =========================
price = get_price(coin)
news = get_news()

st.subheader(f"📊 {coin.upper()} Live Data")
st.metric("Current Price (USD)", price)

# =========================
# CHART DATA (FIXED)
# =========================
url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
params = {"vs_currency": "usd", "days": 1}

response = requests.get(url, params=params)

data = response.json()

prices = data.get("prices", [])

if not prices:
    st.warning("⚠️ No chart data available for this coin")
else:
    df = pd.DataFrame(prices, columns=["time", "price"])

    fig, ax = plt.subplots()
    ax.plot(df["price"])
    ax.set_title(f"{coin.upper()} Price Chart (24H)")
    st.pyplot(fig)

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