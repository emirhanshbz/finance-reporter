import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

SEND_TIME_HOUR = int(os.getenv("SEND_TIME_HOUR", 9))
SEND_TIME_MINUTE = int(os.getenv("SEND_TIME_MINUTE", 0))

REPORTS_DIR = "reports"
DATA_BUNDLE_DIR = "data-bundles"