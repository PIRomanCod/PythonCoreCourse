# module 7 - 15
def flatten(data):
    if not data:
        return []

    if type(data[0]) == list:
        return flatten(data[0]) + flatten(data[1:])

    return [data[0]] + flatten(data[1:])


flatten([1, 2, [3, 4, [5, 6]], 7])