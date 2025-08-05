from app.data_fetcher.stocks import fetch_nasdaq_data
from app.data_fetcher.crypto import fetch_crypto_data
from app.analyzer.sentiment import analyze_market
from app.reporter.formatter import format_report
from app.reporter.emailer import send_email
from app.reporter.archiver import save_report

def daily_job():
    print("🚀 Starting daily job...")

    print("📈 Fetching NASDAQ data...")
    nasdaq_data = fetch_nasdaq_data()

    print("💰 Fetching crypto data...")
    crypto_data = fetch_crypto_data()

    print("🧠 Analyzing data...")
    analysis_results = analyze_market(nasdaq_data, crypto_data)

    print("📝 Formatting report...")
    report = format_report(analysis_results)

    save_report(report)

    print("📤 Sending email...")
    send_email(report)

    print("✅ Daily job completed.")