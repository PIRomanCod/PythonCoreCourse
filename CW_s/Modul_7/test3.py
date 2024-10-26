def decode(data):

    if data == []:
        return None
    if len(data) == 2:
        string = data[0] * data[1]
        return string
    return decode(data[2:])
    #string = (data[0] * data[1])
    # decode(data[2:])
    # else:
    # decode(data[2:])
    # return string + decode(data)
    # _decode(data, string)
    # return _decode(data, string)


data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 4]
print(decode(data))
# data.pop
# print(data[0]*data[1])
