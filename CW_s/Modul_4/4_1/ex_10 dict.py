temp = {
    'name': 'Ivan',
    'age': 33,
    'city': 'Ivano-Frankivsk',
    'data': ['temp', 'new'],
    'dict': {'new': "qqqqq"},
    3: 55,
    (1,): 'trty'
}

print(temp.get('name1111', 'ми не знайшли такий ключ'))

a = temp.get("name1", 'Petro')
a = temp.get("name", 'Petro')
print(a)