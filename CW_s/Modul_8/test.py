# math:
import collections
import math

a = math.log(math.pow(45, -math.sqrt(math.fabs(4)))) * \
    math.sin(45) / math.cos(100)
print(a)
# collection:
"""
Іменовані кортежі
Клас collections.namedtuple дозволяє створити тип даних, що поводиться як кортеж з можливістю привласнити кожному
елементу ім'я, за яким надалі можна отримати доступ
"""

# Point = collections.namedtuple("Point", ['x', 'y', 'qwerty'])
# p = Point(1, 2, 3)
# print(p.x, p.y, p.qwerty)
#
# Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
# cat = Cat("Mark Antoniy", 3, "Jack")
# print(type(cat))
#
# print(f"This is a cat {cat.nickname}, {cat.age} age, his owner is: {cat.owner}")
student = collections.namedtuple("StudentName", ["name", "age", "gender"])
s = student("Ivan", 23, "m")
print(student.__name__)
# print(s.name)
# print(s.age)
# print(s.gender)
