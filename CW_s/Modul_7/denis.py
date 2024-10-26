def decode(data):
    output = ""

    def _decode(data, output):
        while data:
            output = output + data[0] * data[1]
            del data[0]
            del data[0]
            output = _decode(data, output)
        if len(data) == 0:
            return output
        return output
    output_recurs = _decode(data, output)
    print(list(output_recurs))
    return list(output_recurs)


data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 4, "W", 4]
decode(data)
