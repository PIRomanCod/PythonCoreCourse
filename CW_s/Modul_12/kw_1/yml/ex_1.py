import yaml

users = [
    {"name": "Іван", "age": 21, "sex": "male"},
    {"name": "Ірина", "age": 35, "sex": "female"},
    {"name": "Микола", "age": 18, "sex": "male"}
]

serialise = yaml.dump(users)
res = yaml.load(serialise, Loader=yaml.FullLoader)
print(res)

with open("test.yaml", "w", encoding="utf-8") as f:
    yaml.dump({"nginx": users}, f, allow_unicode=True)


with open("test.yaml", "r", encoding="utf-8") as f:
    copy_u = yaml.load(f, Loader=yaml.FullLoader)

print(copy_u)