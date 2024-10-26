# генератор списков
aaa = ['adv', 'dfdf', 'rrr', 'dfsdf', 'rrr', 'rrr', 'sdfdsf', 'rrr']
b = [value for value in aaa if value != 'rrr']

print(b)

# генератор списков
a = [item**2 for item in range(10)]
print(a)
