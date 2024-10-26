import sys

NUMBER_LINES = 3

if len(sys.argv) != 2:
    print("Потрібно передати ім'я файлу")
    quit()

try:
    lines = []
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line in file:  # це то саме що і file.readline()
            lines.append(line)
            if len(lines) > NUMBER_LINES:  # якщо довжина списку більша за константу
                lines.pop(0)  # то удаляємо перші лінії
    print(lines)
except OSError as err:
    print(f"Помилка доступу до файла: {err}")