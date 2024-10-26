'''
Метод: split
Напишемо універсальну функцію get_parameters, яка повертатиме словник з даними.
Оскільки в першому рядку розділити символ ; а на другий &, тому тут вдало підійде
випадок (a|b - відповідає a або b)
'''

import re

url_query = "20850=ot-25-mp-do-47-mp;23777=6-6-5;38435=8-gb;41404=16gb"  # ;
url_search = "q=Cat+and+dog&ie=utf-8&oe=utf-8*aq=t"  # &
url_search_second = "q=Cat+and+dog%ie=utf-8%oe=utf-8%aq=t"  # %

def get_parameters(data: list) -> dict:
    obj_query = {}
    for el in data:
        key, value = el.split("=")  # str
        obj_query.update({key: value.replace("+", " ")})
    return obj_query


data = re.split(r";|&", url_query)
print(data)
data_1 = re.split(r";|&", url_search)
print(data_1)

data_2 = re.split(r";|&|\$|\*", url_search)
print(data_2)

a = get_parameters(data_2)
print(a)