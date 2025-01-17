from pathlib import Path

current_path = Path(".")  # Path()
print(current_path)
print(current_path.cwd())

file = current_path / "bin" / "utils" / "paint.drawio.svg"
print(file)
print(current_path.joinpath("bin", "utils", "paint.drawio.svg"))

print(file.parts)

print(type(file.name))
print(file.name.split(".")[0])

print(file.parent)

print(file.stem)
print(file.suffix)
print(file.suffixes)