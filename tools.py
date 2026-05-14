import requests
import feedparser

def get_price(coin_id="bitcoin"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }

    response = requests.get(url)
    data = response.json()

    if coin_id in data:
        return data[coin_id]["usd"]
    else:
        return "Coin not found"


def get_news():
    url = "https://cointelegraph.com/rss"
    news = feedparser.parse(url)
    return "\n".join([n.title for n in news.entries[:5]])