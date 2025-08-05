def format_report(analysis, news_sentiment, summary_text):
    html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <h2>📊 Daily Financial Market Report</h2>

        <h3>🧠 Summary</h3>
        <p style="background-color:#f5f5f5; padding:10px; border-left:5px solid #007BFF;">
            {summary_text}
        </p>
    """

    # Stocks tablosu
    html += """
        <h3>📈 NASDAQ Stocks</h3>
        <table border="1" cellspacing="0" cellpadding="5">
            <tr>
                <th>Ticker</th>
                <th>Name</th>
                <th>Prev Close</th>
                <th>Today</th>
                <th>Change %</th>
                <th>Sentiment</th>
            </tr>
    """

    for ticker, info in analysis["stocks"].items():
        html += f"""
            <tr>
                <td>{ticker}</td>
                <td>{info['name']}</td>
                <td>{info['previous_close']}</td>
                <td>{info['current_close']}</td>
                <td>{info['change_pct']}%</td>
                <td>{info['sentiment']}</td>
            </tr>
        """

    html += "</table>"

    # Crypto tablosu
    html += """
        <h3>💰 Crypto Markets</h3>
        <table border="1" cellspacing="0" cellpadding="5">
            <tr>
                <th>Coin</th>
                <th>Price (USD)</th>
                <th>Change %</th>
                <th>Sentiment</th>
            </tr>
    """

    for coin, info in analysis["crypto"].items():
        html += f"""
            <tr>
                <td>{coin}</td>
                <td>{info['price']}</td>
                <td>{info['change_pct']}%</td>
                <td>{info['sentiment']}</td>
            </tr>
        """

    html += "</table>"

    # News Sentiment tablosu
    html += """
        <h3>📰 Market News Sentiment</h3>
        <table border="1" cellspacing="0" cellpadding="5">
            <tr>
                <th>Sentiment</th>
                <th>Confidence</th>
                <th>Headline</th>
            </tr>
    """

    for item in news_sentiment:
        html += f"""
            <tr>
                <td>{item['sentiment']}</td>
                <td>{item['score']}</td>
                <td>{item['headline']}</td>
            </tr>
        """

    html += """
        </table>
        <br>
        <p style="font-size: 12px; color: #999;">🕒 This report was generated automatically.</p>
    </body>
    </html>
    """

    return html
