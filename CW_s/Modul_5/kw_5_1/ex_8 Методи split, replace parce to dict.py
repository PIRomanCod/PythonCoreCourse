"""
Методи: split, replace
----
Парсимо query запит для гугла. Тут класичний роздільник & і перетворюємо на словник із даними
"""

url_search = "https://www.google.com/search?q=cat+and+dogs&oq=cat+and+dogs&aqs=chrome&sourceid=chrome&ie=UTF-8"

_, query = url_search.split("?")
print(query)

obj_query = {}
for el in query.split("&"):
    key, value = el.split("=")
    obj_query.update({key: value.replace("+", ' ')})
print(obj_query)


