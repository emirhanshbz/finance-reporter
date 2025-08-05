import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def fetch_finance_headlines():

    print("📰 Fetching new data...")

    params = {
        "category": "business",
        "language": "en",
        "pageSize": 10,
        "apiKey": API_KEY
    }

    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code != 200:
        print("❌ Failed to fetch news:", response.status_code)
        return []
    
    articles = response.json().get("articles", [])
    headlines = [article["title"] for article in articles if article.get("title")]

    return headlines