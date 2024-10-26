class Planes:
    model = None
    country = "UA"

    def __init__(self, name, country, quantity):
        self.name = name
        self.country = country
        self.quantity = quantity


first_plane = Planes("Boeing", "USA", 10)
# name = first_plane.name
# country = first_plane.country
# print(name, country)
second_plane = Planes("F-16", "Turkey", 5)
frache_plane = Planes("Airbus", "France", 2)

our_planes = [first_plane, second_plane, frache_plane]

print([i.quantity for i in our_planes])
print(Planes.country)
