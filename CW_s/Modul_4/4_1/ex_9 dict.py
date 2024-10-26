a = [[1, 2], [1, 4]]
b = dict(a)
print(b)

temp = {
    'name': 'Ivan',
    'age': 33,
    'city': 'Ivano-Frankivsk',
    'data': ['temp', 'new'],
    'dict': {'new': "qqqqq"},
    3: 55,
    (1,): 'trty'
}

new = {'data': 'value'}
temp.update(new)
print(temp)

print("name" in temp)