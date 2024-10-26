from pathlib import Path

new_dir = Path("ABC")
new_dir.mkdir(exist_ok=True)  # exist_ok=True - якщо папка вже існує, то не буде помилки при спробі створити нову
# new_dir.rmdir()  # удаляє папку

# new_dir = Path("Test/Temp")
# new_dir.mkdir(exist_ok=True, parents=True)

list_data = ["First Line", "Hello world", "Test", "happy"]

with open(new_dir / "data", "w", encoding="utf-8") as file:
    for line in list_data:
        file.write(f"{line}\n")

with open(new_dir / "data.avi", "w", encoding="utf-8") as file:
    for line in list_data:
        file.writelines(list_data)