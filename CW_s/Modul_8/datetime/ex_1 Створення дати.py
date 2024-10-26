from datetime import datetime

# Створення дати
date = datetime(year=2022, month=11, day=1)
date = datetime(year=2022, month=11, day=1, hour=19, minute=46, second=15)

print(date)
print(type(date))
print(date.date())
print(date.time())

print(datetime.now().time())
print(datetime.today())
print(date.isoformat())