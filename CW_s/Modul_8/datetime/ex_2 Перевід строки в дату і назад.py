from datetime import datetime

# Перевід строки в дату і назад
td = "28.02.2022"
d = datetime.strptime(td, "%d.%m.%Y")
print(d)
print(type(d))
print(d.date())
print(d.time())

print(d.year, d.month, d.minute)

other_d = d.replace(month=5, day=12, hour=15, minute=55)
print(other_d)
str_d = other_d.strftime("%Y.%d.%m %H:%M==%S")
print(str_d)

a = datetime.now()

print(a.strftime("%Y, %B %e"))
print(a.strftime("%d %y %Y"))