# работа з секундами
from datetime import datetime, MINYEAR, MAXYEAR

d = datetime.now()
print(d.toordinal())  # к-сть днів з 01.01.01
print(d.timestamp())  # к-сть секунд з 01.11.2022 20:19:55 - 01.01.1970