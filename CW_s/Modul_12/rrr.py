def checkio(array: list[int]) -> int:
    if array:
        new_list = [item for item in array[0::2]]
        total = sum(new_list)
        return total * array[-1]
    return 0


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

print(checkio([0, 1, 2, 3, 4, 5])) # == 30
print(checkio([1, 3, 5])) # == 30
print(checkio([6])) # == 36
print(checkio([])) # == 0
