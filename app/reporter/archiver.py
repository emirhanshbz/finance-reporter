import os
from datetime import datetime

def save_report(html_content):
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    date_str = datetime.now().strftime("%Y-%m-%d_%H:%M")
    file_path = os.path.join(reports_dir, f"report_{date_str}.html")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"💾 Report saved to {file_path}")