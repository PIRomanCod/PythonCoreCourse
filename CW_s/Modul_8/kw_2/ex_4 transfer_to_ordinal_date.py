"""
Напишіть функцію, яка приймає на вхід три
цілих числа: день, місяць та рік. Функція має повертати порядковий
номер заданого дня у вказаному році.

Результат функції: номер року та порядковий номер дня у цьому
році - обидва у цілісному форматі.
"""

from datetime import datetime, date

def transfer_to_ordinal_date(day: int, month: int, year: int) -> tuple:
    d = date(year, month, day).toordinal()
    diff = d - date(year, 1, 1).toordinal() + 1  # +1 - це щоб врахувати поточний день
    return year, int(diff)

print(transfer_to_ordinal_date(19, 1, 2022))
print(transfer_to_ordinal_date(19, 2, 2022))
print(transfer_to_ordinal_date(31, 12, 2022))

"""
Розробіть функцію, яка приймає як єдиний параметр порядкову дату, що включає в себе рік і день
по порядку. Як результат функція повинна повертати день і місяць, що відповідають переданій порядковій даті.
"""

def transfer_to_date(ordinal: int, year: int):
    d_temp = date(year, 1, 1).toordinal()
    d = datetime.fromordinal(d_temp - 1 + ordinal)
    return d

print(transfer_to_date(99, 2001))
print(transfer_to_date(365, 2022))