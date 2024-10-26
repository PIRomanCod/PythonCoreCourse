c_codes = {}
# {код країни: імя країни}
import csv
name = 'countries.csv'
with open(name, 'r') as file:
    r = csv.reader(file)
    for line in r:
        c_codes[line[0]] = line[1]
    c_codes.pop("Code")

print(c_codes["UA"])

