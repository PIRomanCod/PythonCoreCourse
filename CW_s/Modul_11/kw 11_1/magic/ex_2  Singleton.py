class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, value):
        self.value = value


foo = Singleton(10)
baz = Singleton(20)
# bar = Singleton(30)


print(foo.value, baz.value)
print(foo, baz)