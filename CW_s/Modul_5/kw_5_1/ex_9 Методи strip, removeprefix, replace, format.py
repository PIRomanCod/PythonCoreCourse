"""
Методи: strip, removeprefix, replace, format
------
Провести валідацію списку телефонів
Телефон: +380501234567 Де: +380 код країни телефон 501234567
Вважаємо, що код валідний з кодом і без коду
"""

phone_storage = ["380991234565", "0631235489", " 380991234444", "611235489", "0000000000", "453664443",
                 '37455859433443', "+38(050)123-45-65", "+38(068)123 45 65", "+38(099)123 bc", "380(66)1234567"]

codes_operators = {"067", "068", "096", "095", "097", "099", "050", "063", "066"}


def is_valid_phone(phone):
    def is_valid_operator(phone) -> bool:
        if phone[:3] in codes_operators:
            return True
        return False

    if phone.isdigit():
        if len(phone) == 12:
            if phone[:2] == "38":
                return is_valid_operator(phone[2:])
        if len(phone) == 10:
            return is_valid_operator(phone)
    return False


def sanitize_phone(phone):
    new_phone = (phone.strip()
                 .removeprefix("+")
                 .replace("(", "")
                 .replace(")", "")
                 .replace(" ", "")
                 .replace("-", "")
                 )
    return new_phone


if __name__ == "__main__":
    for phone in phone_storage:
        phone = sanitize_phone(phone)
        is_valid = is_valid_phone(phone)
        if is_valid:
            print("phone {:>15} is valid".format(phone))
        else:
            print("phone {:>15} is invalid".format(phone))