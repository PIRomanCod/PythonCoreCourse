file = open("test.txt", "w", encoding="utf-8")
file.write("Hello world\n")
file.write("Hello world 1\n")
file.write("Hello world 2\n")
file.writelines(["Hi Jack\n", "Hi David\n", "Hi Bob\n"])
file.close()

file = open("test.txt", "r", encoding="utf-8")
# result = file.read()  # зчитує одразу весь файл у пам'ять
# print(type(result))
# result = file.readline()  # читає одну строку
result = file.readlines()  # читає всі строки і записує їх у список
print(result)
file.close()