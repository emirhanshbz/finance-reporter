import requests

def fetch_crypto_data():
    # İzlenecek kripto paralar (CoinGecko ID'leri)
    coins = ["bitcoin", "ethereum", "solana"]
    vs_currency = "usd"

    print("💰 Fetching crypto data...")

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(coins),
        "vs_currencies": vs_currency,
        "include_24hr_change": "true"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("⚠️ Failed to fetch crypto data.")
        return {}
    
    raw_data = response.json()
    data = {}

    for coin in coins:
        coin_data = raw_data.get(coin)
        if coin_data:
            data[coin.upper()] = {
                "price": round(coin_data[vs_currency], 2),
                "change_pct": round(coin_data[f"{vs_currency}_24h_change"], 2)
            }

    return data