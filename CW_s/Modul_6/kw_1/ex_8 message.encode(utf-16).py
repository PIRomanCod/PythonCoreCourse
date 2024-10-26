from pathlib import Path

message = "Привіт світ! Hello world!"
print(message.encode())  # utf-8 by default for Unix OS

print(message.encode("utf-16"))  # китайці використовують
print(message.encode("cp1251"))  # кодування windows OS
a = message.encode("cp1251")
print(a)
# print(a.decode("cp1251"))
# print(a.decode("utf-16"))
folder = Path("Test")

with open(folder / 'utf-8.txt', 'wb') as f:
    f.write(message.encode())

with open(folder / 'utf-16.txt', 'wb') as f:
    f.write(message.encode("utf-16"))

with open(folder / 'cp1251.txt', 'wb') as f:
    f.write(message.encode("cp1251"))

with open(folder / 'utf-8.txt', 'rb') as f:
    print(f.read().decode())

with open(folder / 'utf-16.txt', 'rb') as f:
    print(f.read().decode("utf-16"))

with open(folder / 'cp1251.txt', 'rb') as f:
    print(f.read().decode("cp1251"))