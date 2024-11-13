import os
from dotenv import load_dotenv
from datetime import datetime
from peewee import *

from peewee import (
    CharField,
    Model,
    DateField,
)


load_dotenv()


DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')


psql_db = PostgresqlDatabase(f'{DB_NAME}', user=f'{DB_USER}', password=f'{DB_PASSWORD}', host=f'{DB_HOST}', port=f'{DB_PORT}')


class BaseModel(Model):
    class Meta:
        database = psql_db


class Request(BaseModel):
    # request_id = IntegerField(primary_key=True)
    request_id = PrimaryKeyField(null=False)
    date = DateField()
    city = CharField()
    temp = CharField()
    feels_like = CharField(null=True)

def db_save(w) -> None:
    req = Request.create(
        date=datetime.now().date(),
        city=w.city,
        temp=w.temp,
        feel_like=w.feels_like

    )
    req.save()
    print(w)

def create_models():
    psql_db.create_tables(BaseModel.__subclasses__())

def drop_tables():
    psql_db.drop_tables(BaseModel.__subclasses__())


