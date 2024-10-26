def formatted_numbers():
    header = "|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary")
    body = []
    body.append(header)
    for num in range(16):
        line = ('|{:<10d}|{:^10x}|{:>10b}|'.format(
            num, num, num))
        body.append(line)

    return body


for el in formatted_numbers():
    print(el)
