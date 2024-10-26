import csv
FILENAME = "users.csv"

users = [
    {"name": "Іван", "age": 21, "sex": "male"},
    {"name": "Ірина", "age": 35, "sex": "female"},
    {"name": "Микола", "age": 18, "sex": "male"}
]

with open(FILENAME, "w", newline="", encoding="utf-8") as file:
    columns = ['name', 'age', 'sex']
    writer = csv.DictWriter(file, delimiter=",", fieldnames=columns)
    writer.writeheader()
    for row in users:
        writer.writerow(row)


with open(FILENAME, 'r', newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print(reader)
    for row in reader:
        print(type(row))
        print(row)