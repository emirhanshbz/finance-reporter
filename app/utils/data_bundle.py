import os
import json

def get_latest_analysis_data():
    reports_dir = "reports"
    files = sorted(f for f in os.listdir(reports_dir) if f.endswith(".json"))
    if not files:
        return {}
    
    latest_file = files[-1]
    json_path = os.path.join(reports_dir, latest_file)

    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)