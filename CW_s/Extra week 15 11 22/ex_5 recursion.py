# module 7 - 17
def encode(data):
    if len(data) == 0:
        return []
    index = 1
    while index < len(data) and data[index] == data[index - 1]:
        index += 1
    current = [data[0], index]
    return current + encode(data[index:len(data)])
