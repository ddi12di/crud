docker run --rm -p 15672:15672 -p 5672:5672 rabbitmq:3.10.7-management  #запуск rabbitMQ на докере

# для запроса id города находятся в файле list_city.json

#task_worker обработчик рэббита и запускает эндпоинты response и delete


#Api на 127.0.0.1/5659
(POST)/ALL получить все запросы на погоду

(GET)/response/{city_id} получить запрос на погоду во внешний сервис в id городе (id городов в list_city.json)

(GET)/response/{city_id} получить запрос на погоду в id городе (id городов в list_city.json)

(GET)/select/{id} получить запрос из истории запросов на погоду по id (id можно получить в бд или энпоинте /all)

(GET)/update/{id}/{name_city} обновить историю запроса по id на другой город (id можно получить в бд или энпоинте /all)

(DEL)/delete/{id} удалить историю запроса по id (id можно получить в бд или энпоинте /all)

(DEL)/drop_db удалить всю базу запросов =)



(POST)/create_tasks/ принимает задачи

    1)На во внешний сервис Weather по id_city(см.list_city.json) обрабатывает и записывает в бд-запросов.
[
    {
        "name": "weather",
        "meta": {
            "city_id": 501175
        }
    },
    {
        "name": "weather",
        "meta": {
            "city_id": 501175
        }
    },
        {
        "name": "weather",
        "meta": {
            "city_id": 501175
        }
    }
]
    2)На удаление в db запросов во внешний сервис Weather по id (id можно получить в бд или энпоинте /all).
[
    {
        "name": "delete",
        "meta": {
            "city_id": 123
        }
    }
]
    3)На удаление в db запросов во внешний сервис Weather.
 [
    {
        "name": "drop_db",
        "meta": {
            "city_id": 0
        }
    }
]


++++++





