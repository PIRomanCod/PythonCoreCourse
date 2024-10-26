name = 'table.csv'

import csv

# with open(name, 'w') as file:
#     w = csv.writer(file)
#     for i in range(1, 21):
#         w.writerow([i, i**2, i**3])


with open(name, 'r') as file:
    r = csv.reader(file)
    # r = csv.DictReader(file)
    res = []
    for line in r:
        res.append(line)

print(res)