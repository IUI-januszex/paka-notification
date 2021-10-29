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
    'receiver_email': "michal.zawadzki66669@gmail.com", 
    'name': 'michal',
    'surname': 'zawadzki',
    'numberParcel': '453255',
    'pin': '123',
    'date': '20 paz 2019',
    'link':"link"
}
o=RabbitMqSend()
o.send(message)