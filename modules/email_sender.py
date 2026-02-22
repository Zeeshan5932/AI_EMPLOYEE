import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config


def handle_email(task):
    task_type = task.get("type")

    if task_type == "send_email":
        receiver = task.get("to")
        subject = task.get("subject")
        body = task.get("body")

        try:
            msg = MIMEMultipart()
            msg["From"] = config.EMAIL_ADDRESS
            msg["To"] = receiver
            msg["Subject"] = subject

            msg.attach(MIMEText(body, "plain"))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
            server.send_message(msg)
            server.quit()

            return "Email sent successfully."

        except Exception as e:
            return f"Failed to send email: {str(e)}"

    return "Email task not supported."