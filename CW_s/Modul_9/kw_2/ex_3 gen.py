def my_range(limit):
    value = 0
    while value < limit:
        yield value
        value += 1  # value = value + 1

for num in range(5):
    print(num)
print("==========")
for num in my_range(5):
    print(num)

gen = my_range(5)

while True:
    try:
        r = next(gen)
        print(r)
    except StopIteration:
        break

print("!" * 15)