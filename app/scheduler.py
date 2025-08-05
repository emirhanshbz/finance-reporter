from app.data_fetcher.stocks import fetch_nasdaq_data
from app.data_fetcher.crypto import fetch_crypto_data
from app.data_fetcher.news import fetch_finance_headlines
from app.analyzer.sentiment import analyze_market
from app.analyzer.news_sentiment import analyze_headlines
from app.analyzer.summarizer import generate_summary
from app.reporter.formatter import format_report
from app.reporter.emailer import send_email
from app.reporter.archiver import save_report

def daily_job():
    print("🚀 Starting daily job...")

    # 1. Verileri çek
    print("📈 Fetching NASDAQ data...")
    nasdaq_data = fetch_nasdaq_data()

    print("💰 Fetching crypto data...")
    crypto_data = fetch_crypto_data()

    print("📰 Fetching news data...")
    news_headlines = fetch_finance_headlines()

    # 2. Verileri analiz et
    print("🧠 Analyzing data...")
    analysis_results = analyze_market(nasdaq_data, crypto_data)

    print("🧠 Analyzing news data...")
    news_sentiment = analyze_headlines(news_headlines)

    # 3. Özet üret
    raw_text = "Today’s market summary: "
    # 3. AI özet için metin hazırlama
    raw_text = "Today’s market summary: "

    # Stocks
    for ticker, info in analysis_results["stocks"].items():
        change = info["change_pct"]
        direction = (
            "rose" if change > 0 else
            "fell" if change < 0 else
            "remained unchanged"
        )
        raw_text += f"{ticker} {direction} by {abs(change)}%. "

    # Crypto
    for coin, info in analysis_results["crypto"].items():
        change = info["change_pct"]
        direction = (
            "increased" if change > 0 else
            "decreased" if change < 0 else
            "stayed flat"
        )
        raw_text += f"{coin.title()} {direction} to ${info['price']} ({change}%). "

    # News sentiment (opsiyonel): pozitif haberlerden biri
    positive_headlines = [n["headline"] for n in news_sentiment if n["sentiment"].lower() == "positive"]
    if positive_headlines:
        raw_text += f"Positive news included: \"{positive_headlines[0]}\". "


    print("📝 Generating summary...")
    summary = generate_summary(raw_text)

    # 4. Raporu oluştur
    print("📄 Formatting report...")
    report = format_report(analysis_results, news_sentiment, summary)

    # 5. Raporu kaydet ve gönder
    print("💾 Saving report...")
    save_report(report)
    send_email(report)

    print("✅ Daily job completed.")
