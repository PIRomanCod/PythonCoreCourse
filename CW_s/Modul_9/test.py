def amount_payment(self):
    sum = 0
    [sum += value for value in self if value > 0]
    return sum


print(amount_payment([1, -3, 4]))
