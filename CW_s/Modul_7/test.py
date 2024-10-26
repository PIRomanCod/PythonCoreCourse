class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __len__(self):
        return sorted(self.cart)

    def __bool__(self):
        return len(self.cart) > 0

    def __str__(self):
        return f"cart: {self.cart}, customer:{self.customer})"

    def __add__(self, extra):
        new_cart = self.cart.copy()
        new_cart.append(extra)
        return Order(new_cart, self.customer)

    def __getitem__(self, key):
        return self.cart[key]

    def __setitem__(self, key, value):
        # if key in self.cart:
        #     self.cart[key].append(value)
        self.cart + value


order1 = Order(["mers", "bmw"], "Abeda")
order2 = Order([], "WWWW")
# print(bool(order2))

# for order in [order1, order2]:
#     if order:
#         print(f"{order.customer}")
order2 += "fdfff"
# print(order3)
print(order2[0])
print(order1[1])
order1["mers"]["WWWW"]