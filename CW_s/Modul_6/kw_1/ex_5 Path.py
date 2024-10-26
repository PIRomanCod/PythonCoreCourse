from pathlib import Path

folder = Path("./Temp")
filename = folder / "temp.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:  # with open("Temp/temp.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
except OSError as e:
    print(f"Помилка доступу до файлу: {e}")
finally:
    print("\nFile operation completed")
