source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]


def save_applicant_data(source, output):  # output
    item_list = []
    string = ""

    for item in source:
        for v in item.values():
            string += str(v) + ","

        string = string[0:-1]
        item_list.append(string)
        string = ""
    print(item_list)

    with open(output, "w") as fh:
        for item in item_list:
            item += "\n"
            fh.write(item)


save_applicant_data(source, r"applicant_data.txt")
