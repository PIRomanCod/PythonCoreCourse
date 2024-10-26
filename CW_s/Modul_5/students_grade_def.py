grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    completed = []
    for item, (key, value) in enumerate(students.items(), 1):
        completed.append("{:>4}|{:<10}|{:^5}|{:^5}".format(
            item, key, value, grades[value]))
    return completed


for el in formatted_grades(students={"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}):
    print(el)
