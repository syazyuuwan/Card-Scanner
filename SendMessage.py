import smtplib
import os
from email.mime.text import MIMEText

class SendMessage:
    def send_email(recipient_email, subject, body):
        # Replace with your actual Google API key (security risk!)
        api_key = os.getenv("EMAIL_PASSWORD")

        message = MIMEText(body, "plain")
        message["Subject"] = subject
        message["From"] = os.getenv("EMAIL_ADDRESS")  # Replace with your sender email
        message["To"] = recipient_email

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(message["From"], api_key)
                server.sendmail(message["From"], message["To"], message.as_string())
                print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")