import sys


def parse_args():
    result = ""
    path = sys.argv[1:]

    for args in path:
        result = result + " " + args
    result = result.lstrip()

    return result


print(parse_args("C: \Python\Go_IT\)
