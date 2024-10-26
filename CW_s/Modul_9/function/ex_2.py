# Функція як об'єкт першого класу
# Друга вимога - Функція може бути передана в іншу функцію як аргумент

def mul(a, b):
    return a * b

def add(a, b):
    return a + b


def ops(a, b, func):  # func - передаємо ф-цію як параметр
    return func(a, b)


result_mul = ops(a=2, b=4, func=mul)
print(result_mul)

result_add = ops(2, 4, add)
print(result_add)