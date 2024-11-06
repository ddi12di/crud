import json
list_city = {}

with open('current.city.json', encoding='utf8') as f:
    json_city = json.load(f)


    for i in json_city:
        a = 1
        if i['id']:
            a =+ 1
            city = i['name']
            print(city)
            id = i['id']
            print(id)
            list_city = dict.fromkeys(city, id)

            print(list_city)

            if a>100:
                break
























    with open('Base.json', 'r', encoding="utf-8") as fh:
        data = json.load(fh)
        data["Пользователь 1"]["Имя"] = "Что-то тут"
        with open('Base.json', "w", encoding="utf-8") as f:
            json.dump(data, f, separators=(',', ': '), sort_keys=True, indent=4, ensure_ascii=True)


