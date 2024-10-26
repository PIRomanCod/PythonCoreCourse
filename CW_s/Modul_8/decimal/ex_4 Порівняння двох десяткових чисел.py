"""
Порівняння двох десяткових чисел
Значення 0 вказує, що обидва числа дорівнюють,
значення 1 вказує, що перше число більше за друге число,
а значення -1 вказує, що перше число менше за друге.
"""
from decimal import Decimal

print(Decimal("1.2").compare(Decimal("1.2")))

print(0.1 + 0.2 == 0.3)

num1 = Decimal("0.1") + Decimal("0.2")
num2 = Decimal("0.3")
print(num1.compare(Decimal(0.3)))

print(Decimal(0.1) + Decimal(0.2) == Decimal(0.3))
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))