'''
Метод: sub
'''

import re

string = "The Java best Java language is Java"

print(re.sub(r"Java", "Python", string, count=30))