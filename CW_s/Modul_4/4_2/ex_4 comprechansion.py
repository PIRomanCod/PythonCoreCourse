nums = [x for x in range(21) if x % 2 == 0 or x % 5 == 0]
print(nums)

test = ['Test' if item % 2 == 0 else "Hello" for item in range(20)]
print(test)

l = [1, 2, 3, 4, 5]


a = [True if item == 1 else False if item == 2 else None if item == 3 else " " for item in l]

n = []
for item in l:
    if item == 1:
        n.append(True)
    else:
        if item == 2:
            n.append(False)
        else:
            if item == 3:
                n.append(None)
            else:
                n.append(" ")
print(n)