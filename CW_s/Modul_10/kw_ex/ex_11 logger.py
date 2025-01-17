#: result: [ім'я функції][результат]\n
# """
import sys


def logger(func):
    call_count = 0

    def inner(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        sys.stdout.write(f" call [{call_count}]: [{func.__name__}][{args}]\n")
        result = func(*args, **kwargs)
        sys.stdout.write(f" result: [{func.__name__}][{result}]\n")
        return result
    return inner


@logger
def add(x, y):
    return x + y


@logger
def mul(x, y):
    return x * y


print(add(3, 5))
print(mul(3, 5))
print(add(4, 10))
print(mul(4, 10))
print(add(5, 5))
print(mul(5, 5))
