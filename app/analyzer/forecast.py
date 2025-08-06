import yfinance as yf
from prophet import Prophet
import pandas as pd

def forecast_bitcoin(days=7):
    # BTC verisi
    btc = yf.Ticker("BTC-USD")
    hist = btc.history(period="180d") # 6 aylık geçmiş

    if hist.empty:
        print("⚠️ No BTC data available.")
        return []
    
    # Prophet formatına çevirme
    df = hist.reset_index()[["Date", "Close"]]
    df["Date"] = df["Date"].dt.tz_localize(None)
    df.columns = ["ds", "y"]

    # Model eğitimi
    model = Prophet()
    model.fit(df)
    
    # Gelecek tarihleri oluşturma
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)

    # Son N gün tahmini
    result = forecast.tail(days)[["ds", "yhat", "yhat_lower", "yhat_upper"]]

    # Biçimleme
    result = result.round(2)
    forecast_data = result.to_dict(orient="records")

    return forecast_data


def generate_forecast_comment(forecast_data):
    if not forecast_data or len(forecast_data) < 2:
        return "Forecast data is insufficient to determine a trend."
    
    start_price = forecast_data[0]["yhat"]
    end_price = forecast_data[-1]["yhat"]

    change_pct = ((end_price - start_price) / start_price) * 100

    if change_pct > 2:
        trend = "a noticeable increase"
    elif change_pct > 0.5:
        trend = "a gradual upward trend"
    elif change_pct < -2:
        trend = "a significant decrease"
    elif change_pct < -0.5:
        trend = "a gradual downward trend"
    else:
        trend = "a stable trend with minimal fluctuation"

    return f"Bitcoin is expected to follow {trend} over the next 7 days, starting at around ${start_price:.2f} and reaching approximately ${end_price:.2f}."