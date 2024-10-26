"""
Метод: isdigit
----
1. Знайти кількість цифр у рядку
2. Знайти кількість чисел у рядку
"""
string = "Нильс Бор родился в семье профессора физиологии Копенгагенского университета Христиана Бора (1858--1911), " \
    "дважды становившегося кандидатом на Нобелевскую премию по физиологии и медицине[10], и Эллен Адлер (" \
    "1860--1930), дочери влиятельного и весьма состоятельного еврейского банкира и парламентария-либерала Давида " \
    "Баруха Адлера (дат. David Baruch Adler; 1826--1878) и Дженни Рафаэль (1830--1902) из британской еврейской " \
    "банкирской династии Raphael Raphael & sons[en][11]. Родители Бора поженились в 1881 году. 2"


def count_digits(string):
    count = 0
    for el in string:
        if el.isdigit():
            count += 1
    return count


print(count_digits(string))


def count_numbers(string):
    count = 0
    pos = 0
    nums = []
    while pos < len(string):
        if string[pos].isdigit():  # перевірямо чи строка є числом
            num = ''
            # шукаємо закінчення числа
            while pos < len(string) and string[pos].isdigit():
                num += string[pos]  # записуємо число
                pos += 1  # збільшуємо позиції на 1
            nums.append(num)
            count += 1  # збільшуємо лічильник на 1
        else:
            pos += 1
    return count, nums  # повертаємо tuple


print(count_numbers(string))
