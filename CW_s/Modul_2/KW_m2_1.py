from re import A


a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

if a < b:
    temp = a
    a = (a + b) / 2
    b = temp * b

else:
    temp = b
    b = (a + b) / 2
    a = temp * a
print(a, b)

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
if a < b:
    a, b = (a + b) / 2, a * b

else:
    b, a = (b + a) / 2, b * a
print(a, b)
