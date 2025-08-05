def analyze_market(nasdaq_data, crypto_data):
    
    print("🧠 Analyzing data...")
    
    def label_change(change_pct):
        if change_pct > 1:
            return "📈 Positive"
        elif change_pct < -1:
            return "📉 Negative"
        else:
            return "Neutral"
        

    analysis = {}

    # NASDAQ
    analysis["stocks"] = {}

    for ticker, info in nasdaq_data.items():
        sentiment = label_change(info["change_pct"])
        analysis["stocks"][ticker] = {
            **info,
            "sentiment": sentiment
        }

    # Crypto
    analysis["crypto"] = {}

    for coin, info in crypto_data.items():
        sentiment = label_change(info["change_pct"])
        analysis["crypto"][coin] = {
            **info,
            "sentiment": sentiment
        }

    return analysis
        