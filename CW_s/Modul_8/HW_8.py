# Вам треба реалізувати корисну функцію для виведення списку колег, яких потрібно привітати з днем народження на тижні.
# список словників users, кожен словник у ньому обов'язково має ключі name та birthday.
# Така структура представляє модель списку користувачів з їх іменами і днями народження.
# name — це рядок з ім'ям користувача, а
# birthday — це datetime об'єкт, в якому записаний день народження

# Ваше завдання написати функцію get_birthdays_per_week,
# яка отримує на вхід список users і виводить у консоль (за допомогою print)
# список користувачів, яких потрібно привітати по днях.

# get_birthdays_per_week виводить іменинників у форматі:
# Monday: Bill, Jill
# Friday: Kim, Jan
from datetime import datetime, timedelta, date
from collections import defaultdict


users = [{"Bill": datetime(year=2012, month=11, day=2)},
         {"Oleg": datetime(year=2009, month=11, day=2)},
         {"Jill": datetime(year=2009, month=11, day=3)},
         {"Vasyl": datetime(year=2009, month=11, day=3)},
         {"Kim": datetime(year=2001, month=11, day=4)},
         {"Nikolay": datetime(year=2001, month=11, day=4)},
         {"Jan": datetime(year=1997, month=11, day=5)},
         {"Petro": datetime(year=1999, month=11, day=5)},
         {"Jack": datetime(year=1980, month=11, day=6)},
         {"Mykola": datetime(year=1985, month=11, day=6)},
         {"Will": datetime(year=1981, month=11, day=7)},
         {"Smith": datetime(year=1990, month=11, day=7)},
         {"Gil": datetime(year=1991, month=11, day=8)},
         {"Gul": datetime(year=1995, month=11, day=8)},
         {"Murat": datetime(year=1998, month=11, day=9)},
         {"Lola": datetime(year=1970, month=11, day=10)},
         {"Kola": datetime(year=1975, month=11, day=11)},
         {"Nika": datetime(year=1987, month=11, day=23)}]

weekdays = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]


def get_birthdays_per_week(users, weekdays) -> dict:
    list_of_birthdays = []
    current_datetime = datetime.today()
    current_datetime = current_datetime.date()
    current_datetime = date(year=current_datetime.year,
                            month=current_datetime.month, day=current_datetime.day+1)
    one_weeks_interval = timedelta(days=6)
    end_of_view = current_datetime + one_weeks_interval
    print(current_datetime, end_of_view)
    for item in users:
        for key, value in item.items():
            value = value.date()
            if current_datetime.month <= value.month <= end_of_view.month:
                if current_datetime.day <= value.day <= end_of_view.day:
                    new_date = date(year=current_datetime.year,
                                    month=value.month, day=value.day).weekday()
                    list_of_birthdays.append([weekdays[new_date], key])
    grouped_words = defaultdict(list)

    for word in list_of_birthdays:
        char = word[0]
        grouped_words[char].append(word[1])
    res = dict(grouped_words)

    for key, value in res.items():
        print(f"{key}: {', '.join(value)}")


get_birthdays_per_week(users, weekdays)
