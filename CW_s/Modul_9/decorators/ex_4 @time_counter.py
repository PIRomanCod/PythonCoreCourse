# Зробити декоратор, який повертає кортеж з результатом функції обчислення факторіал та часом її виконання

from time import time, sleep

def time_counter(func):
    def interval(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        diff = time() - start
        return result, diff
    return interval

@time_counter
def test_func(a, b):
    sleep(b)
    return a + b

print(test_func(3, 10))
print(test_func(4, 2))
#
# @time_counter
# def factorial(n, cache={}):
#     if n < 0:
#         raise ValueError("Number can't be negative")
#
#     def calc(n):
#         result = 1
#         for val in range(1, n + 1):
#             if val in cache:  # перевіряємо чи результат вєе є у кеші?
#                 result = cache[val]  # то беремо результат з кеша (з словника)
#                 print(f"{val} in cache {result}")
#             else:
#                 result = val * cache.get(val - 1, 1)  # щоб не було помилки
#                 cache[val] = result  # присвоюю результат
#                 print(f"{val} not in cache {result}")
#         return result
#     return calc
#
#
# f3 = factorial(1300)
# print(f"f(3): {f3}")
#
# f5 = factorial(1300)
# print(f"f(5): {f5}")
#
# f4 = factorial(4)
# print(f"f(4): {f4}")