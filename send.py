# from pika import *
#
# def con(body):
#     connection = BlockingConnection(
#         ConnectionParameters(host='localhost'))
#     channel = connection.channel()
#
#     channel.queue_declare(queue='hello')
#
#     channel.basic_publish(exchange='', routing_key='hello', body=body )
#     print(" [x] Sent new message!'")
#     connection.close()
#



