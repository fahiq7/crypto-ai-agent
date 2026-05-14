import requests
import feedparser

def get_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    data = requests.get(url).json()
    return data[coin_id]["usd"]


def get_news():
    url = "https://cointelegraph.com/rss"
    news = feedparser.parse(url)
    return "\n".join([n.title for n in news.entries[:5]])