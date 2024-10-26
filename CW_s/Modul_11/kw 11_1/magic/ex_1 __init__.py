# class Foo:
#     def __init__(self, price):
#         print("Конструктор Foo")
#         self.price = price
#
#
# class Baz(Foo):
#     def __init__(self, price):
#         super().__init__(price)
#
# baz = Baz(100)

class Foo:  # class Foo(object)

    def __init__(self, value):
        print("Конструктор класу Foo")
        self.value = value
    def __new__(cls, *args, **kwargs):
        print("Метод new класу Foo")
        instance = super(Foo, cls).__new__(cls)
        return instance

class Baz(Foo):
    def __init__(self, value):
        super(Baz, self).__init__(value)

baz = Baz(10)  # __new__ -> __init__
foo = Baz(20)

print(baz.value, foo.value)