import os
from datetime import datetime
from app import config
import json

def save_report(html_content, analysis=None, news_sentiment=None, summary=None, btc_forecast=None, forecast_comment=None):
    date_str = datetime.now().strftime("%Y-%m-%d")
    reports_dir = config.REPORTS_DIR

    os.makedirs(reports_dir, exist_ok=True)

    # HTML kaydet
    html_path = os.path.join(reports_dir, f"{date_str}.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # JSON veri arşivi (chatbot için)
    if all(v is not None for v in [analysis, news_sentiment, summary, btc_forecast, forecast_comment]):
        data = {
            "stocks": analysis.get("stocks", {}),
            "crypto": analysis.get("crypto", {}),
            "news_sentiment": news_sentiment,
            "summary": summary,
            "btc_forecast": [
                {
                    "ds": row["ds"].strftime("%Y-%m-%d") if hasattr(row["ds"], "strftime") else str(row["ds"]),
                    "yhat": row["yhat"],
                    "yhat_lower": row["yhat_lower"],
                    "yhat_upper": row["yhat_upper"]
                }
                for row in btc_forecast
            ],
            "forecast_comment": forecast_comment
        }

        json_path = os.path.join(reports_dir, f"{date_str}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
