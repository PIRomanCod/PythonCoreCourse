def checkio(food: int) -> int:

    if 0 < food < 10**5:
        fed = 0
        new = 1
        if 1 < food <= 3:
            return 2
        while food >= (fed + new):
            fed += new
            food -= fed
            new += 1

        return fed


print(checkio(1))  # == 1
print(checkio(3))  # == 2
print(checkio(5))  # ) == 3
# print(checkio(6))  # ) ==
# print(checkio(7))  # ) ==
# print(checkio(8))  # ) ==
print(checkio(10))  # == 6
print(checkio(18))  # ) == 3
# print(checkio(30))
# print(checkio(40))
# print(checkio(50))
