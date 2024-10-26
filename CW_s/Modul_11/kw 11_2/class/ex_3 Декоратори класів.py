# Декоратори класів

def method_decorator(func):
    def wrapper(self, *args):
        print("=method_decorator run=")
        result = func(self, *args)
        print("=method_decorator end=")
        return result
    return wrapper

def class_decorator(cls):
    print("=class_decorator run=")
    new_cls = cls
    new_cls.value = 45
    return new_cls

@class_decorator
class TestClass:
    name = "TestClass"

    @method_decorator
    def info(self, user):
        return f"Hello {user}. This is {self.name}"

t = TestClass()
print(t.info("Ivan"))
print(t.value)
t.test = 10
print(t.test)