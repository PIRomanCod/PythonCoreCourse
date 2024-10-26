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
        if age in list(range(0, 50)):
            self.__age = age
        else:
            raise ValueError("Тварини стільки не живуть")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Тварини повинні мати якусь вагу")

# chup = Animal("Chupacabra", 12, 100)
# print(chup.name, chup.age, chup.weight)


chup = Animal("Chupacabra", -3, 100)
chup.age = -5
print(chup.name, chup.age, chup.weight)
