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

# def send_email(email: str, subject: str, body: str) -> None:

#     try:
    
#         # add MIME headers
#         message = MIMEMultipart()
#         message["From"] = EMAIL_FROM
#         message["To"] = email
#         message["Subject"] = subject
#         message.attach(MIMEText(body, "plain"))

#         # send email
#         context = ssl.create_default_context()
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#             server.login(EMAIL_FROM, EMAIL_PASSWORD)
#             server.sendmail(EMAIL_FROM, email, message.as_string())

#     except Exception as e:
#         print("here")
#         print(str(e))
