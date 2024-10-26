# Функція як об'єкт першого класу
# Третя вимога - функція може бути повернена з функції як результат

def mul(a, b):
    return a * b

def add(a, b):
    return a + b

def ops(operator: str):
    if operator == "*":
        return mul
    elif operator == "+":
        return add
    else:
        raise ValueError("Operator not supported")

try:
    f_mul = ops("*")
    print(f_mul)
    result = f_mul(3, 5)
    print(result)
except ValueError:
    print("Operator '*' failed")


try:
    f_add = ops("+")
    print(f_add)
    result = f_add(3, 5)
    print(result)
except ValueError:
    print("Operator '*' failed")


try:
    f_div = ops("/")
    print(f_div)
    result = f_div(3, 5)
    print(result)
except ValueError:
    print("Operator '/' failed")


f_div = ops("/")
print(f_div)
result = f_div(3, 5)
print(result)


