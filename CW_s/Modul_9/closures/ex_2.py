# Closures

def taxer(base_tax):  # Податки
    def calculate(money):
        nonlocal base_tax
        if money >= 10_000:   # Якщо заробили більше 10 000
            base_tax = 1.5 * base_tax  # змінюємо ставку податку
        return money - base_tax * money
    return calculate


ukr = taxer(0.1)  # %
swd = taxer(0.55)  # %

money_ukr_1 = ukr(15000)
money_swd = swd(25000)
money_ukr_2 = ukr(5000)

print(money_ukr_1, money_swd, money_ukr_2)
