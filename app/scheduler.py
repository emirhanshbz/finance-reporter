from app.data_fetcher.stocks import fetch_nasdaq_data
from app.data_fetcher.crypto import fetch_crypto_data
from app.data_fetcher.news import fetch_finance_headlines
from app.analyzer.sentiment import analyze_market
from app.analyzer.news_sentiment import analyze_headlines
from app.reporter.formatter import format_report
from app.reporter.emailer import send_email
from app.reporter.archiver import save_report

def daily_job():
    print("🚀 Starting daily job...")

    # Veri Çek  
    nasdaq_data = fetch_nasdaq_data()
    crypto_data = fetch_crypto_data()
    news_headlines = fetch_finance_headlines()

    # Analiz
    analysis_results = analyze_market(nasdaq_data, crypto_data)
    news_sentiment = analyze_headlines(news_headlines)

    # Rapor
    report = format_report(analysis_results, news_sentiment)

    # Arşivle ve e-posta gönder
    save_report(report)
    send_email(report)

    print("✅ Daily job completed.")