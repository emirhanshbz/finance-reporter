import yfinance as yf
import pandas as pd

def fetch_nasdaq_data():
    # Örnek NASDAQ hisseleri
    tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN"]

    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d") # Son 2 gün
        if len(hist) < 2:
            continue

        yesterday = hist.iloc[-2]
        today = hist.iloc[-1]

        change_pct = ((today["Close"] - yesterday["Close"]) / yesterday["Close"])
        data[ticker] = {
            "name": stock.info.get("shortName", ticker),
            "previous_close": round(yesterday["Close"], 2),
            "current_close": round(today["Close"], 2),
            "change_pct": round(change_pct, 2)
        }

    return data
