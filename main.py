from tools import get_price, get_news
from agents import run_agent

# Choose coin here
coin = "ethereum"   # change: bitcoin, solana, binancecoin, etc.

price = get_price(coin)
news = get_news()

print(f"\nAnalyzing: {coin.upper()}")
print(f"Price: ${price}")

market_analysis = run_agent(
    "Market Analyst",
    f"Analyze {coin} price trend and prediction",
    price
)

news_analysis = run_agent(
    "News Analyst",
    f"Analyze how news affects {coin}",
    news
)

sentiment_analysis = run_agent(
    "Sentiment Analyst",
    f"Detect sentiment for {coin}",
    news
)

final_input = f"""
Coin: {coin}
Price: {price}

Market Analysis:
{market_analysis}

News Analysis:
{news_analysis}

Sentiment:
{sentiment_analysis}
"""

final_decision = run_agent(
    "Senior Crypto Strategist",
    f"Give BUY/SELL/HOLD decision for {coin} with confidence score",
    final_input
)

print("\n===== FINAL DECISION =====\n")
print(final_decision)