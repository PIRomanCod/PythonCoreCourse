from functools import reduce

numbers = [5, 6, 7]

sum_nums = reduce(lambda x, y: x + y, numbers, 0)  #1крок: x=0, y=5 => x=5 => | 2крок x=5, y=6 => x=11 | 3крок x=11, y=7 => x=18
print(sum_nums)

sum_nums = reduce(lambda x, y: x * y, numbers, 1)  #1крок: x=1, y=5 => x=5 => | 2крок x=5, y=6 => x=30 | 3крок x=30, y=7 => x=210
print(sum_nums)

greeting = reduce(lambda calc, next: calc + next, ['h', 'e', 'l', 'l', 'o'], '')
print(type(greeting))
print(greeting)