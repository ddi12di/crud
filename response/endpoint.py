import os
from fastapi import APIRouter
import pika
from dataclasses import asdict
from storage.db import Request, db_save, create_models, drop_tables
from response.response import weather
from model.model import TasksRequest, Task
import json
from dotenv import load_dotenv

view_app = APIRouter()

load_dotenv()

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')


@view_app.post('/all')
async def all_tables():
    create_models()

    def all_table():
        return Request.select()

    try:
        reqs = all_table()
        dick = []
        for req in reqs:
            dick.append({
                'requestID': req.request_id,
                'city': req.city,
                'temp': req.temp,

            })
        return dick
    except:
        return 'Empty'


@view_app.get('/response/city_id')
def response(city_id: int):
    create_models()
    w = weather(city_id)
    db_save(w)
    return 200


@view_app.get('/select/{id}')
def select_id(id):
    create_models()
    selectID = Request.get(Request.request_id == id)
    return selectID


@view_app.get('/update/{id}/{name_c}')
def update_city(id, name_c):
    create_models()
    update_city = Request.get(Request.request_id == id)
    update_city.city = name_c
    update_city.save()
    return 200


@view_app.get('/delete/{id}')
def delete_city(id):
    create_models()
    try:
        delete_city = Request.get(Request.request_id == id)
        delete_city.delete_instance()
        return 200
    except:
        return 'No result'


@view_app.get('/drop_db')
def drop_db():
    drop_tables()
    return '200=)'


@view_app.post('/create_tasks/')
def created_tasks(tasks: list[TasksRequest]):
    def conn(body):
        rmq_user = os.getenv('RABBITMQ_USER')
        rmq_pass = os.getenv('RABBITMQ_PASSWORD')
        rmq_host = os.getenv('RABBITMQ_HOST')

        credentials = pika.PlainCredentials(rmq_user, rmq_pass)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=rmq_host,
                credentials=credentials
            )
        )
        channel = connection.channel()
        channel.queue_declare(queue='hello', durable=True)

        channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(body).encode('utf8'))
        print(f" [x] Sent new message {body}!'")
        connection.close()

    tasks = [Task(**t.dict()) for t in tasks]
    for task in tasks:
        conn(asdict(task))

    return 200
