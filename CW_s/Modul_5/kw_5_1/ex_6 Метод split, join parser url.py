"""
Метод: split, join
----
Парсимо URL с Rozetka
"""

url_query = "20850=ot-25-mp-do-47-mp;23777=6-6-5;38435=8-gb;41404=16gb"

query = url_query.split(';')
print(query)

obj_query = {}
for el in query:
    key, value = el.split('=')
    obj_query[key] = value
    # obj_query.update({key: value})

print(obj_query)

prepare = []
for key in obj_query:
    print(f"key is: {key}")
    print(f"value is: {obj_query[key]}")
    print(f"result: {key + '=' + obj_query[key]}")
    prepare.append(f"{key}={obj_query[key]}")
    # prepare.append(key + "=" + obj_query[key])
print(';'.join(prepare))