import csv
with open("names.csv", "w", newline="\n") as csvfile:  # newline == `\n` - заміна
    fieldnames = ["first_name", "last_name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # окремо записуємо заголовок

    writer.writeheader()
    writer.writerow({"first_name": "First Name 1", "last_name": "Last Name 1"})
    writer.writerow({"first_name": "First Name 2", "last_name": "Last Name 2"})
    writer.writerow({"last_name": "Last Name 3", "first_name": "First Name 3"})


with open("names.csv") as file:
    print(file.read())