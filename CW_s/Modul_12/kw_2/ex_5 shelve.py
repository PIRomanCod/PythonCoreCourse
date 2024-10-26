import shelve

class AwesomeClass:
    awesome = True

class Dummy:
    default = 0

    def __init__(self, value):
        self.default = value


aw = AwesomeClass()
dum = Dummy(42)

filename = 'database/some_db'  # розширення не потрібно

with shelve.open(filename) as db:
    db['awesome'] = aw  # зберігаємо по ключах
    db['dummy'] = dum  # зберігаємо по ключах
    db['my_list'] = [1, 2, 3, 4]  # зберігаємо по ключах

    temp = db["my_list"]
    temp.append(5)
    db["my_list"] = temp  # оновлюємо

    daw = db['awesome']  # це буде копія
    print(id(aw), id(daw))
    del db["awesome"]  # удаляємо значення


print("-----")
with shelve.open(filename) as states:
    for key in states:
        print(f'{key}: {states[key]}')
    print(states["my_list"])
    print(states["dummy"].default)
