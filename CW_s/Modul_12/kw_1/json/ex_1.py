import json

d = {"a": 1}
l = [1, 2.2]
t = (3, 5)  # стане списком, і ним залишиться після десеріалізації
s = "Some string"
b = True  # буде з малої літери, потім повернеться у нормальний вигляд
# st = {1, 2, "Test"}  потрібно руками змінити тип
obj = {"tuple": t, "list": l, "dict": d, "string": s, "bool": b, "NA": None, "int": 55}

print(json.dumps(d))
print(json.dumps(l))
print(json.dumps(t))
print(json.dumps(s))
print(json.dumps(b))
# print(json.dumps(st))

with open('storage.json', 'w') as f:
    json.dump(obj, f)