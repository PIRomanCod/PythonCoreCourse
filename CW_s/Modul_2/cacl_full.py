result = None
operand = None
operator = None
wait_for_number = True
wait_for_operator = True
wait_for_end = True
sub_dict = {"sub_result": 0, "sub_operator": None}


while wait_for_end == True:

    try:
        while wait_for_number == True:
            number = input("Enter your number: ")
            operand = float(number)

            if result == None:
                sub_dict["sub_result"] = operand
                result = sub_dict.get("sub_result")
            else:
                if operator == "+":
                    result = sub_dict.get("sub_result") + operand
                    sub_dict["sub_result"] = result

                elif operator == "-":
                    result = sub_dict.get("sub_result") - operand
                    sub_dict["sub_result"] = result

                elif operator == "*":
                    result = sub_dict.get("sub_result") * operand
                    sub_dict["sub_result"] = result

                elif operator == "/":
                    result = sub_dict.get("sub_result") / operand
                    sub_dict["sub_result"] = result

                elif operator == "=":
                    print(f"Result := {result}")

                    wait_for_number = False
                    wait_for_operator = True

    except ValueError:
        print(f"'{number}' is not a number. Try again.")
        wait_for_operator = False

    while wait_for_operator == True:
        operator = input("Enter operator'+,-,*,/'. For result push=: ")

        if operator != "+" and operator != "-" and operator != "/" and operator != "*" and operator != "=":
            while operator != "+" and operator != "-" and operator != "/" and operator != "*" and operator != "=":
                print(f"'{operator}' is not '+' or '-' or '/' or '*'. Try again")
                operator = input("Enter operator'+,-,*,/'. For result push=: ")

                if operator == "+":
                    wait_for_operator = False
                    wait_for_number = True

                elif operator == "-":
                    wait_for_operator = False
                    wait_for_number = True

                elif operator == "*":
                    wait_for_operator = False
                    wait_for_number = True

                elif operator == "/":
                    wait_for_operator = False
                    wait_for_number = True

                elif operator == "=":
                    wait_for_operator = False
                    wait_for_number = True
                    print(f"Result := {result}")
                    break

        elif operator == "+":
            wait_for_operator = False
            wait_for_number = True

        elif operator == "-":
            wait_for_operator = False
            wait_for_number = True

        elif operator == "*":
            wait_for_operator = False
            wait_for_number = True

        elif operator == "/":
            wait_for_operator = False
            wait_for_number = True

        elif operator == "=":
            wait_for_operator = False
            wait_for_number = True
            wait_for_end = False
            print(f"Result := {result}")
            break
