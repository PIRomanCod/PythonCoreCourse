"""
Метод: isdigit
----
Заданий список, кожним елементом якого є рядок символів, що складається з одних цифр.
Впорядкувати елементи масиву за зростанням їх числових значень і вивести на екран.
Від максимального елемента відібрати значення мінімального та вивести різницю на екран.
Підрахувати середнє значення всіх елементів.
"""

numbers = ["123", "456", "321", "10", "75", "abc", "23c"]

def senitize(data):
    result = []
    for el in data:
        if el.isdigit():
            result.append(el)
    return result

def transform_to_int(data):
    result = []
    for el in data:
        result.append(int(el))
    return result

san_nums = senitize(numbers)
san_nums = transform_to_int(san_nums)
san_nums.sort()
print(san_nums)

print(max(san_nums) - min(san_nums))
print(sum(san_nums) / len(san_nums))