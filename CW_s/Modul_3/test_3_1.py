def get_grade(key):

    points = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
    grade = points.get(key)
    return grade


def get_description(key):

    points = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough",
              "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}
    description = points.get(key)
    return description


print(get_grade("B"))
print(get_description("B"))
