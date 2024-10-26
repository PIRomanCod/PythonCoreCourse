def encode(data):
    output = ""
    data = "".join(data)

    def encode(data, output):
        currCh = data[:1]
        currCount = 1
        while data:
            for ch in data[1:]:
                if ch != currCh:
                    output += (currCh + str(currCount))
                    currCh = ch
                    currCount = 1
                else:
                    currCount += 1

            output = encode(data[len(output):], output)
        if len(data) == 0:
            return output
        return output
    output_recurs = encode(data, output)
    print(list(output_recurs))
    return list(output_recurs)


data = ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y',
        'Y', 'Z', 'Z', 'Z', 'Z', 'W', 'W', 'W', 'W']
encode(data)
