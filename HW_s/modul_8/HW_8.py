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


users = [{"name": "Bill", "birthday": datetime(year=2012, month=11, day=2)},
         {"name": "Oleg", "birthday": datetime(year=2009, month=11, day=2)},
         {"name": "Jill", "birthday": datetime(year=2009, month=11, day=3)},
         {"name": "Vasyl", "birthday": datetime(year=2009, month=11, day=3)},
         {"name": "Kim", "birthday": datetime(year=2001, month=11, day=4)},
         {"name": "Nikolay", "birthday": datetime(year=2001, month=11, day=4)},
         {"name": "Jan", "birthday": datetime(year=1997, month=11, day=5)},
         {"name": "Petro", "birthday": datetime(year=1999, month=11, day=5)},
         {"name": "Jack", "birthday": datetime(year=1980, month=11, day=6)},
         {"name": "Mykola", "birthday": datetime(year=1985, month=11, day=6)},
         {"name": "Will", "birthday": datetime(year=1981, month=11, day=7)},
         {"name": "Smith", "birthday": datetime(year=1990, month=11, day=7)},
         {"name": "Gil", "birthday": datetime(year=1991, month=11, day=8)},
         {"name": "Gul", "birthday": datetime(year=1995, month=11, day=8)},
         {"name": "Murat", "birthday": datetime(year=1998, month=11, day=9)},
         {"name": "Lola", "birthday": datetime(year=1970, month=11, day=10)},
         {"name": "Kola", "birthday": datetime(year=1975, month=11, day=11)},
         {"name": "Nika", "birthday": datetime(year=1987, month=11, day=23)}]

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

    for user in users:
        new_date_for_user = date(
            year=current_datetime.year,
            month=user.get('birthday').month,
            day=user.get('birthday').day)

        if current_datetime <= new_date_for_user <= end_of_view:
            new_date = new_date_for_user.weekday()
            if new_date in (5, 6):
                new_date = 0
            list_of_birthdays.append([weekdays[new_date], user.get("name")])
        grouped_words = defaultdict(list)

    for word in list_of_birthdays:
        char = word[0]
        grouped_words[char].append(word[1])
    res = dict(grouped_words)

    for key, value in res.items():
        print(f"{key}: {', '.join(value)}")


if __name__ == '__main__':
    get_birthdays_per_week(users, weekdays)
