'''
Метод: sub
Дано рядок символів.
Виключити з цього рядка групи символів між дужками [, ].
Самі дужки теж мають бути виключені.
'''

import re
string = "Виключити із цієї [групи] символів, [розташовані між] дужками [, ]."

print(re.sub(r"\[.*?\]", "", string))

