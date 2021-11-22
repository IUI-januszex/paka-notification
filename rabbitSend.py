#!/usr/bin/env python
import pika
import json

class RabbitMqSend():
    def __init__(self):
        self.nameQueue='januszex'

    def send(self,message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=self.nameQueue)

        channel.basic_publish(exchange='', routing_key=self.nameQueue, body=json.dumps(message))
        print(" [x] Sent message")
        connection.close()


message = {
    'emailAddress': "michal.zawadzki66669@gmail.com", 
    'parcelId': "7584643347634",
    'notificationType': "PARCEL_WILL_RETURN", 
    'sender': 'mirek',
    'receiver': 'krzysiek',
    'pin': None,
    'arrivalDate': None
}
o=RabbitMqSend()
o.send(message)