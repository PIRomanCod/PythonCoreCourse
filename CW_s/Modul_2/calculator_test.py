result = None
operand = None
operator = None
wait_for_number = True
wait_for_operator = True
wait_for_end = True
_dict = {"sub_result": 0, }

while wait_for_end:
    try:
        while wait_for_number == True:
            number = input("Enter your number: ")
            operand = float(number)
            _dict["sub_result"] = operand
            wait_for_number = False
            wait_for_operator = True

        print(_dict.get("sub_result"))
        break

    except ValueError:
        print(f"{number} not a number. Try again.")
