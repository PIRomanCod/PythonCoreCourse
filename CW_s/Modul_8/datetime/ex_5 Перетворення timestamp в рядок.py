# Перетворення timestamp в рядок
from datetime import datetime

timestamp = 1658857176.546034
print(type(timestamp))

date_time = datetime.fromtimestamp(timestamp)
print(date_time)
str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
print(str_date_time)
str_time = date_time.strftime("%I %p %M:%S")
print(str_time)