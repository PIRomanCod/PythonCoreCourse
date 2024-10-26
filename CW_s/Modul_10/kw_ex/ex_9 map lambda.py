nums = [i for i in range(1, 10)]
print(nums)
sq = map(lambda x: x ** 2, nums)

result = filter(lambda value: bool(value % 2), sq)
print(list(result))

sq = map(lambda x: x ** 2, nums)
result = filter(lambda value: not bool(value % 2), sq)
print(list(result))

result = filter(lambda value: bool(value % 2), map(lambda x: x ** 2, [i for i in range(1, 10)]))
print(list(result))

result = map(lambda x: x ** 2, filter(lambda value: bool(value % 2), [i for i in range(1, 10)]))
print(list(result))