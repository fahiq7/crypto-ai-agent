import requests
import feedparser

import requests

import requests

def get_price(coin_id):
    url = "https://api.coingecko.com/api/v3/simple/price"

    try:
        r = requests.get(url, params={
            "ids": coin_id,
            "vs_currencies": "usd"
        })

        data = r.json()

        # SAFE CHECK
        return data.get(coin_id, {}).get("usd", None)

    except:
        return None


def get_news():
    url = "https://cointelegraph.com/rss"
    news = feedparser.parse(url)
    return "\n".join([n.title for n in news.entries[:5]])