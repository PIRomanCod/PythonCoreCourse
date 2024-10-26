"""
Методи: split, replace
"""
phone = "+1-234-567-89-10"

# replace(old, new)

edited_phone = phone.replace("-", " ")
print(edited_phone)  # +1 234 567 89 10


edited_phone = phone.replace("-", "")
print(edited_phone)  # +12345678910


edited_phone = phone.replace("-", "", 3)  # 3 - к-сть змін(три символа буде заменено)
print(edited_phone)  # +1234-567-89-10
