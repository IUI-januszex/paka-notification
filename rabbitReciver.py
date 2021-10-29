#!/usr/bin/env python
import pika, sys, os, json
from MailHTML import MailHTML
from SenderMail import SenderMail
def main():
    nameQueue='januszex'
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=nameQueue)
    def callback(ch, method, properties, body):
        jsonData=json.loads(body)
        receiver_email=jsonData['receiver_email']
        name=jsonData['name']
        surname=jsonData['surname']
        numberParcel=jsonData['numberParcel']
        pin=jsonData['pin']
        date=jsonData['date']
        link=jsonData['link']
        mailHTML=MailHTML(name=name,surname=surname,numberParcel=numberParcel,pin=pin,date=date,link=link)
        html = mailHTML.generateHTML()
        senderMail=SenderMail(receiver_email,html)
        senderMail.sendMail()
        print("mail wyslany do ",receiver_email)

    channel.basic_consume(queue=nameQueue, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)