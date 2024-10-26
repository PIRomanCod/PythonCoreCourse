from copy import copy, deepcopy
# copy.copy(x) - повертає поверхневу копію x
# copy.deepcopy(x) - повертає повну (глибоку копію)

# l = [1, 2, 3, ['a', 'b', 'c']]
l = [1, 2, 3, ['a', 'b', 'c']]

test_l = l[:]
l_copy = copy(l)
l_deep = deepcopy(l)

print(l == l_copy, l is l_copy)

l[0] = 5
print(l, test_l, l_copy, l_deep)
l[3][0] = "test"
print(l, test_l, l_copy, l_deep)


class A:
    def __init__(self, a):
        self.a = a
        self.c = None
        self.b = True

    def test(self):
        return "test"

a = copy(A(4))
a.test()
# a1 = A(5)
# a1.test()
b = deepcopy(a)
print(b.test())