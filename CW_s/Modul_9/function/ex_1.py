# Функція як об'єкт першого класу
# Перша вимога - Функція може бути збережена у змінній чи структурі даних

def mul(a, b):
    return a * b


f = mul  # збереження ф-ції у змінній
result = f(2, 3)  # викликаємо ф-цію через змінну
print(result)

field = {
    "a": 2,
    "b": 3,
    "func": f
}
n = field.get("func")
print(n)
result = field.get("func")(field.get("a"), 11)
print(result)

result = field.get("func")(5, 6)
print(result)
