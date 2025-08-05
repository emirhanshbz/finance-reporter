def format_report(analysis):
    html = """
    <html>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <h2>📊 Daily Financial Market Report</h2>
        
        <h3>NASDAQ Stocks</h3>
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

    html += """
        </table>

        <h3>Crypto Markets</h3>
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

    html += """
        </table>
        <br>
        <p>🕒 This report was generated automatically.</p>
    </body>
    </html>
    """

    return html