numbers = []

for item in range(21):
    if item % 2 == 0:
        numbers.append(item)
print(numbers)


numbers_1 = [item for item in range(21) if item % 2 == 0]
print(numbers_1)

names = ['Ivan', 'Petro', 'Oksana', 'Iryna', 'Stas', 'Igor']
new_names = [item for item in names if 'a' in item]
print(new_names)
