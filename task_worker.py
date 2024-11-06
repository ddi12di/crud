import json
from pika import BlockingConnection, ConnectionParameters
from response.endpoint import response, delete_city, drop_db


def proccessing(ch, method, properties, body: bytes):
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
    elif body['name'] == 'drop':
        drop_db()
        print(f'Congratulations, the database has been deleted')
    else:
        print(f'error')



def complete_queue():
    connection = BlockingConnection(ConnectionParameters(
        host='127.0.0.1', port=5672
    ))

    channel = connection.channel()
    channel.queue_declare('hello')

    channel.basic_consume(queue='hello', on_message_callback=proccessing, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':

    while True:
        try:
            count = complete_queue()
        except Exception as e:
            print(e)
