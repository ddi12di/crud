import json
import pika, sys, os
from response.endpoint import response, delete_city, drop_db
from dotenv import load_dotenv

load_dotenv()

rmq_user = os.getenv('RABBITMQ_USER')
rmq_pass = os.getenv('RABBITMQ_PASSWORD')
rmq_host = os.getenv('RABBITMQ_HOST')


def callback(ch, method, properties, body):
    print(f" [x] Recieved {body}")
    body = body.decode('utf8')
    body = json.loads(body)
    print(body)
    print('---------------')
    print(body['meta']['city_id'])

    if body['name'] == 'weather':
        response(body['meta']['city_id'])
        print(f'Proccesed task DONE')
    elif body['name'] == 'delete':
        delete_city(body['meta']['city_id'])
        print(f'DELETE request DONE')
    elif body['name'] == 'drop_db':
        drop_db()
        print(f'Congratulations, the database has been deleted')
    else:
        print(f'error')


rmq_user = os.getenv('RABBITMQ_USER')
rmq_pass = os.getenv('RABBITMQ_PASSWORD')
rmq_host = os.getenv('RABBITMQ_HOST')


def main_work():
    print('устанавливаем')
    print(rmq_pass,rmq_user,rmq_host)
    credentials = pika.PlainCredentials(rmq_user, rmq_pass)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=rmq_host,
            credentials=credentials,
            connection_attempts=10,
            retry_delay=5,
            socket_timeout=10
        )
    )

    channel = connection.channel()

    channel.queue_declare(queue='hello', durable=True)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print('установили')
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    while True:
        try:
            count = main_work()
        except Exception as e:
            print(e)
