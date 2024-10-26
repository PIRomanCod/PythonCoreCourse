def is_all_upper(text: str) -> bool:
    text = text.replace(" ", "")
    if not text:
        return True
    elif text.isnumeric():
        return True
    elif text.isupper():
        return True
    return False


print(is_all_upper("ALL UPPER"))  # == True
print(is_all_upper("all lower"))  # == False
print(is_all_upper("mixed UPPER and lower"))  # == False
print(is_all_upper(""))  # == True
print(is_all_upper("444"))  # == True
print(is_all_upper("55 55 5 "))  # == True

# ch = "A"
# if ord(ch) in range(65, 90) or ord(ch) == 20:
#     print("Yes")
# else:
#     print(ord(ch))