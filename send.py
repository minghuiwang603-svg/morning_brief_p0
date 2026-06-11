import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email(subject: str, body: str) -> None:
    user = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASSWORD")
    to = os.environ.get("TO_EMAIL")
    msg = MIMEText(body)
    msg["Subject"] =subject
    msg["From"]=user
    msg["To"]=to
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(user, password)
        server.sendmail(user, to, msg.as_string())

if __name__ == "__main__":
    send_email("晨报测试", "hello from Python")
