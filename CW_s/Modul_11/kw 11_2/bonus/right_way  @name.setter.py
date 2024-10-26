class Animal:
    def __init__(self, nickname, age, weight):
        # self.__nickname = nickname
        # self.__age = age
        # self.__weight = weight
        self.__nickname = None
        self.__age = None
        self.__weight = None

        self.name = nickname
        self.age = age
        self.weight = weight

    @property
    def name(self):
        return self.__nickname

    @name.setter
    def name(self, nickname):
        if len(nickname) > 0:
            self.__nickname = nickname
        else:
            raise ValueError("Тварина повинна мати імя")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Тварини повинні мати якусь вагу")


class Turtle(Animal):
    def __init__(self, nickname, age, weight):
        super().__init__(nickname, age, weight)

    @Animal.age.setter
    def age(self, age):
        if age in list(range(0, 150)):
            Animal.age.fset(self, age)
            # super(Turtle, type(self)).age.fset(self, age)
        else:
            raise ValueError("Тваринки стільки не живуть")

# turtle = Turtle("Tortila", 12, 100)
turtle = Turtle("Tortila", 149, 100)
print(turtle.name, turtle.age, turtle.weight)