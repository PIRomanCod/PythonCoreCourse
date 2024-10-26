e_tuple = ()
print(e_tuple)
print(type(e_tuple))

a = ('test', 'new', 'tmp', 'code')
print(a)
print(type(a))

*tt, a_2 = a
# print(a_1)
print(a_2)
print(tt)
# print(a_4)

a = [1, 4, 6]
b = tuple(a)
print(b)

