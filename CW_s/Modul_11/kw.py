class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


vector = Vector(3, 4)
print(str(vector))
print(repr(vector))
new_var = eval(str(vector))
new_var2 = eval(repr(vector))
print(type(new_var))
print(type(new_var2))
