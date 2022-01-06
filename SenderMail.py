from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
import os


class SenderMail():
    def __init__(self,receiver_email,html):
        self.receiver_email=receiver_email
        self.html=html
    
    def sendMail(self):
        # sender_email = "januszex.kurier@gmail.com"
        # receiver_email = self.receiver_email
        # password = 'januszex123'

        sender_email = "januszex.3547635@gmail.com"
        receiver_email = self.receiver_email
        password = 'JanuszeX7645'

        message = MIMEMultipart()
        message["Subject"] = "Parcel from Januszex"
        message["From"] = sender_email
        message["To"] = receiver_email

        message.attach(MIMEText(self.html, "html"))
        msgBody = message.as_string()

        server = SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msgBody)
        server.quit()