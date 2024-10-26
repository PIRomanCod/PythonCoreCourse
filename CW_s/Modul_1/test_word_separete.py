# программа которая делит текст на слова
text = input("Your text: ")
word = ""

for char in text:

    if char == " ":
        print(word)
        word = ""
    else:
        word += char
print(word)
