"""
Метод: find
----
Дано рядок символів.
Виключити з цього рядка групи символів між дужками [, ].
Самі дужки теж мають бути виключені.
Передбачається, що в кожній парі дужок немає інших дужок.
"""

string = "Виключити із цієї [рядки групи] символів, [розташовані між] дужками [, ]."

# start_index = string.find('[')
# end_index = string.find(']')
#
# new_str = string[:start_index] + string[end_index + 1]
# print(new_str)

def sanitize(string):
    new_string = string[:]
    while True:
        start_index = new_string.find('[')
        end_index = new_string.find(']')
        if start_index == -1:
            break
        new_string = new_string[:start_index] + new_string[end_index + 1:]
    return new_string


print(sanitize(string))

