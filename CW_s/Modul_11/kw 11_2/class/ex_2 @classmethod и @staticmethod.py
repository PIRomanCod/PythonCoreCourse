"""
Розбираємо різницю між: звичайним методом, @classmethod и @staticmethod
"""

class DecoratorTest:

    def doubler(self, x):
        print("Множення на 2")
        print("Множення на 2: %s" % self)
        return x * 2

    @classmethod
    def triples(cls, x):
        print("Множення на 3")
        print("Множення на 3: %s" % cls)
        return x * 3

    @staticmethod
    def quad(x):
        print("Множення на 4")
        return x * 4

decor = DecoratorTest()
print("===Екземпляр класу===")
print(decor.doubler(4))
print(decor.triples(4))
print(decor.quad(4))
print("===Виклик через клас===")
# print(DecoratorTest.doubler(4))
print(DecoratorTest.triples(4))
print(DecoratorTest.quad(4))