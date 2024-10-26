x = [1, 2, 3, 4, 5]

header = "{:>4}|{:<10}|{:^5}|{:^5}\n".format("x", "x^2", "x^3", "xz")
spliter = "=" * len(header)
body = ""
for num in x:
    line = "{:>4}|{:<10}|{:^5}|{:^5}\n".format(num, num**2, num**3, num**4)
    body += line + "\n"
result = "".join([header, spliter, body])

print(result)
