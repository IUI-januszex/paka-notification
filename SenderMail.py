import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SenderMail():
    def __init__(self,receiver_email,html):
        self.receiver_email=receiver_email
        self.html=html
    
    def sendMail(self):
        sender_email = "januszex.kurier@gmail.com"
        receiver_email = self.receiver_email
        password = 'januszex123'

        message = MIMEMultipart("alternative")
        message["Subject"] = "Parcel from Januszex"
        message["From"] = sender_email
        message["To"] = receiver_email


        text = MIMEText(self.html, "html")

        message.attach(text)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )