

def encode(data):
    def _encode(data):
        data = "".join(data)
        if not data:
            return ""
        first = data[0]
        counter = 0

        for letter in data:
            if letter != first:
                break
            counter += 1
        result = f"{first}{counter}" + _encode(data[counter:])
        # result = list(result)
        return result
    res = list(_encode(data))
    output = []
    for item in res:
        if item.isdigit():
            output.append(int(item))
        else:
            output.append(item)

    return output


data = ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y',
        'Y', 'Z', 'Z', 'Z', 'Z', 'W', 'W', 'W', 'W']
print(encode(data))

# ['X', '3', 'Z', '2', 'X', '2', 'Y', '3', 'Z', '2']
# ['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]
