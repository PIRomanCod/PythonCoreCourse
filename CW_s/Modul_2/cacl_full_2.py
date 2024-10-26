result = None
operand = None
operator = None
wait_for_number = True
wait_for_operator = True
wait_for_end = True
_dict = {"sub_result": 0, "sub_operator": None}


while wait_for_end == True:

    try:
        while wait_for_number == True:
            number = input("Enter your number: ")
            operand = float(number)

            if result == None:
                _dict["sub_result"] = operand
                result = _dict.get("sub_result")
            else:
                if operator == "+":
                    result = _dict.get("sub_result") + operand
                    _dict["sub_result"] = result

                elif operator == "-":
                    result = _dict.get("sub_result") - operand
                    _dict["sub_result"] = result

                elif operator == "*":
                    result = _dict.get("sub_result") * operand
                    _dict["sub_result"] = result

                elif operator == "/":
                    result = _dict.get("sub_result") / operand
                    _dict["sub_result"] = result

                elif operator == "=":
                    print(result)
                    # break

            #_dict["sub_result"] = operand
            #sub_result2 = _dict.get("sub_result")
            wait_for_number = False
            wait_for_operator = True

            # print(_dict.get("sub_result"))

            # break

    except ValueError:
        print(f"{operand} not a number. Try again.")
        wait_for_operator = False

    #operator = input("Enter operator'+,-,*,/'. For result push=: ")
    # print(operator, wait_for_number, operand)

    while wait_for_operator == True:
        operator = input("Enter operator'+,-,*,/'. For result push=: ")
    # print(operator, wait_for_number, operand)
        if operator != "+" and operator != "-" and operator != "/" and operator != "*" and operator != "=":
            # print("Zaeeeee....")
            #operator = input("Enter operator'+,-,*,/'. For result push=: ")
            # :
            while operator != "+" and operator != "-" and operator != "/" and operator != "*" and operator != "=":
                print(f"{operator}is not '+' or '-' or '/' or '*'. Try again")
                operator = input("Enter operator'+,-,*,/'. For result push=: ")

                if operator == "+":
                    #print("entered +")
                    wait_for_operator = False
                    wait_for_number = True

                elif operator == "-":
                    #print("entered -")
                    wait_for_operator = False
                    wait_for_number = True

                elif operator == "*":
                    #print("entered *")
                    wait_for_operator = False
                    wait_for_number = True

                elif operator == "/":
                    #print("entered /")
                    wait_for_operator = False
                    wait_for_number = True

                elif operator == "=":
                    # print("entered =")  # result = operand
                    # wait_for_end = False
                    wait_for_operator = False
                    wait_for_number = True
                    print(result)
                    break

        elif operator == "+":
            #print("entered +")
            wait_for_operator = False
            wait_for_number = True

        elif operator == "-":
            #print("entered -")
            wait_for_operator = False
            wait_for_number = True

        elif operator == "*":
            #print("entered *")
            wait_for_operator = False
            wait_for_number = True

        elif operator == "/":
            #print("entered /")
            wait_for_operator = False
            wait_for_number = True

        elif operator == "=":
            # print("entered =")  # result = operand
            wait_for_operator = False
            wait_for_number = True
            wait_for_end = False
            print(result)
            break
