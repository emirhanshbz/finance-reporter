import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app import config

def send_email(html_content):
    try:
        print("📤 Sending email to", config.RECEIVER_EMAIL)
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "📊 Daily Financial Market Report"
        msg["From"] = config.EMAIL_USER
        msg["To"] = config.RECEIVER_EMAIL

        msg.attach(MIMEText(html_content, "html"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(config.EMAIL_USER, config.EMAIL_PASS)
        server.sendmail(config.EMAIL_USER, config.RECEIVER_EMAIL, msg.as_string())
        server.quit()

        print("✅ Email sent successfully.")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")