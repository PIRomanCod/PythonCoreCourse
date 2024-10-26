import sys

NUMBER_LINES = 3

if len(sys.argv) != 2:
    print("Потрібно передати ім'я файлу")
    quit()

try:
    file = open(sys.argv[1], "r", encoding="utf-8")
    # line = file.readline()
    count = 0
    while count < NUMBER_LINES:
        line = file.readline().strip()
        # line = line.strip()  # відкидає пробіли, табуляцію і т.д.
        count += 1
        print(line)
    file.close()
except OSError as err:
    print(f"Помилка доступу до файла: {err}")
