# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import smtplib
# import ssl


import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail, To
import urllib.parse

from env_vars import EMAIL_FROM, EMAIL_ORG_NAME, FRONTEND_URL, SENDGRID_API_KEY
from exceptions.exceptions import EmailNotSentException


sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)

def send_account_creation_confirmation_email(dest_email_addr: str, user_id: str, user_name: str = "") -> None:
    
    email_confirmation_url: str = urllib.parse.urljoin(FRONTEND_URL, f"/confirm/{user_id}")
    subject: str = "Account creation confirmation"
    body: str = f"Please confirm your account by clicking the following link: {email_confirmation_url}"
    send_email(dest_email_addr, subject, body, user_name)


def send_password_reset_email(email: str, reset_token: str) -> None:
    reset_url: str = urllib.parse.urljoin(FRONTEND_URL, f"/reset_password/{reset_token}")
    subject: str = "Password reset"
    body: str = f"Please reset your password by clicking the following link: {reset_url}"
    send_email(email, subject, body)


def send_email(email: str, subject: str, body: str, user_name: str = "") -> None:

    try:
        # https://sendgrid.com/docs/for-developers/sending-email/sender-identity/
        from_email = Email(EMAIL_FROM, EMAIL_ORG_NAME)
        to_email = To(email, user_name or None)
        content = Content("text/plain", body)
        mail = Mail(from_email, to_email, subject, content)
        sg.send(mail)
    except Exception as e:
        print(str(e))
        raise EmailNotSentException("Email could not be sent")


def is_valid_email_addr(email_address: str) -> bool:
    return "@" in email_address  # TODO: improve this
