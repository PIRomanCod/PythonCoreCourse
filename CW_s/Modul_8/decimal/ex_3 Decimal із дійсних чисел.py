# Створення Decimal із дійсних чисел

from decimal import Decimal
num_1 = 1.37
num_2 = 1.5

first = Decimal.from_float(num_1)
second = Decimal.from_float(num_2)

print(first, second)

first = Decimal(str(num_1))
second = Decimal(str(num_2))
print(first, second)

first = Decimal(num_1)
second = Decimal(num_2)
print(first, second)