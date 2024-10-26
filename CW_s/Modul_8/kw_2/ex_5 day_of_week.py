# Написати функцію, яка визначає який день тижня у певної дати у вигляді "день-місяць-рік".

from datetime import datetime
# import calendar
# print(calendar.isleap(2020))  перервіряє чи рік є високосним

days_name = {
   0: "понеділок",
   1: "вівторок",
   2: "середа",
   3: "четвер",
   4: "п'ятниця",
   5: "субота",
   6: "неділя",
}

def day_of_week(date: str):
   d, m, y = date.split("-")
   date = datetime(day=int(d), month=int(m), year=int(y))
   d_name = days_name.get(date.weekday())
   return d_name

print(day_of_week("31-01-2005"))
print(day_of_week("25-05-1990"))
print(day_of_week("10-12-1988"))
print(day_of_week("03-11-2022"))
