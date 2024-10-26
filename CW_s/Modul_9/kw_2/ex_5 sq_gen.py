sq_gen = (i ** 2 for i in range(10))
print(sq_gen)

# a = list(sq_gen)
# print(a)

for i in sq_gen:
    print(i, " ", end="")
