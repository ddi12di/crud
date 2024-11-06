import json
dict_list = []

with open('current.cit.json', 'r', encoding='utf8') as f:
    json_city = json.load(f)

    for i in json_city:
        list_city = {}
        if i['id']:
            city = i['name']
            id = i['id']
            list_city.update(dict(city=city, id=id))
            dict_list.append(list_city)





with open('list_city.json', 'w',  encoding='utf8') as f:
    json.dump(dict_list, f, indent=4)







# with open('Base.json', 'r', encoding="utf-8") as fh:
#     data = json.load(fh)
#     data["Пользователь 1"]["Имя"] = "Что-то тут"
#     with open('Base.json', "w", encoding="utf-8") as f:
#         json.dump(data, f, separators=(',', ': '), sort_keys=True, indent=4, ensure_ascii=True)
#

    # city = i['name']
    # print(city)
    # id = i['id']
    # print(id)



#
# with open('Base.json', 'r', encoding="utf-8") as fh:
#     data = json.load(fh)
#     data["Пользователь 1"]["Имя"] = "Что-то тут"
#     with open('Base.json', "w", encoding="utf-8") as f:
#         json.dump(data, f, separators=(',', ': '), sort_keys=True, indent=4, ensure_ascii=True)


