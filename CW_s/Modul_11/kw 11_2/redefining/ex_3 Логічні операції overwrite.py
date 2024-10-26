# Логічні операції

class Car:
    def __init__(self, year, mark, model, color, price):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ne__(self, other):
        return self.price != other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

car_a = Car(2017, "BMW", "X5", "Black", 5500)
car_b = Car(2020, "Tesla", "Model S", "White", 45500)

print(car_a == car_b)
print(car_a < car_b)
print(car_a > car_b)
print(car_a != car_b)
print(car_a <= car_b)
print(car_a >= car_b)