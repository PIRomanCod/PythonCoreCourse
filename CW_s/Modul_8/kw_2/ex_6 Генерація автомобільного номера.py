"""
Генерація автомобільного номера. Дві літери, чотири цифри, дві літери.
Для Київська області код АI
Останні дві літери зі списку: A, B, C, E, H, I, K, M, O, P, T, X
(використовуються українські літери, що мають графічні відповідники у латиниці)
"""

import random

start = "AI"
set_of_letters = ["A", "B", "C", "E", "H", "I", "K", "M", "O", "P", "T", "X"]
set_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

first_l = "".join(random.choices(set_of_letters, k=2))
numbers = "".join(random.choices(set_of_numbers, k=4))
last_l = "".join(random.choices(set_of_letters, k=2))

print(f"{first_l} {numbers} {last_l}")

print(
    f"{''.join(random.choices(set_of_letters, k=2))} "
    f"{''.join(random.choices(set_of_numbers, k=4))} "
    f"{''.join(random.choices(set_of_letters, k=2))}")
