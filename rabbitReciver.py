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
        try:
            jsonData=json.loads(body.decode("utf-8"))
            receiverEmail=jsonData['emailAddress']
            typeMessage=jsonData['notificationType']
            allowedTypesMessage=["PARCEL_REGISTERED_SENDER","PARCEL_REGISTERED_RECEIVER","COURIER_WILL_ARRIVE","PARCEL_DELIVERED","PARCEL_WILL_ARRIVE_TODAY"]
            if (typeMessage in allowedTypesMessage):
                mailHTML=MailHTML(typeMessage)
                html = mailHTML.generateHTML(jsonData)
                senderMail=SenderMail(receiverEmail,html)
                senderMail.sendMail()
                print("mail wyslany do ",receiverEmail)
            else:
                print("Not correct type of message",receiverEmail)
        except:
            print("Mail not send")



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