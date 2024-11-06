import os
from dotenv import load_dotenv
from model.model import  Weather_model
import requests


load_dotenv()


KEY = os.environ.get('KEY')
ID = os.environ.get('ID')
UNITS = os.environ.get('UNITS')
LANG = os.environ.get('LANG')
BASE_URL = os.environ.get('BASE_URL')


def weather(city_id: int) -> Weather_model:
    response = requests.get(
        f'{BASE_URL}?id={city_id}&appid={KEY}&units={UNITS}&lang={LANG}'
    )
    all_response = response.json()

    ##TEST- при недоступности ресурса
    # all_response = {
    #     "coord": {
    #         "lon": 39.4139,
    #         "lat": 57.1914
    #     },
    #     "weather": [
    #         {
    #             "id": 801,
    #             "main": "Clouds",
    #             "description": "небольшая облачность",
    #             "icon": "02n"
    #         }
    #     ],
    #     "base": "stations",
    #     "main": {
    #         "temp": 1.46,
    #         "feels_like": 13.84,
    #         "temp_min": 1.01,
    #         "temp_max": 14.46,
    #         "pressure": 1032,
    #         "humidity": 72,
    #         "sea_level": 1032,
    #         "grnd_level": 1017
    #     },
    #     "visibility": 10000,
    #     "wind": {
    #         "speed": 2.25,
    #         "deg": 140,
    #         "gust": 2.32
    #     },
    #     "clouds": {
    #         "all": 23
    #     },
    #     "dt": 1726512767,
    #     "sys": {
    #         "country": "RU",
    #         "sunrise": 1726455326,
    #         "sunset": 1726501143
    #     },
    #     "timezone": 10800,
    #     "id": 501183,
    #     "name": "Ростов",
    #     "cod": 200
    # }

    temp = all_response['main']['temp']
    feels_like = all_response['main']['feels_like']
    city = all_response['name']

    w = Weather_model(temp, feels_like, city)

    return w

