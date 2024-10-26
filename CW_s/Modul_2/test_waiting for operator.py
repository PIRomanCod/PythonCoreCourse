operand = 0
operator = input("Enter operator'+,-,*,/'. For result push=: ")
# print(operator, wait_for_number, operand)

if operator != "+" and operator != "-" and operator != "/" and operator != "*" and operator != "=":
    print("Zaeeeee....")
    operator = input("Enter operator'+,-,*,/'. For result push=: ")
    # :
    while operator != "+" and operator != "-" and operator != "/" and operator != "*" and operator != "=":
        print("Zaeeeee....")
        operator = input("Enter operator'+,-,*,/'. For result push=: ")

        if operator == "+":
            print("entered +")
            # result = result + operand
            # number = input("Enter your number: ")
            # operand = float(number)
            # result = result + operand
            # operator = input("Enter operator'+,-,*,/'. For result push=: ")

        elif operator == "-":
            print("entered -")
            # result = result - operand
            # number = input("Enter your number: ")
            # operand = float(number)
            # result = result - operand
            # operator = input("Enter operator'+,-,*,/'. For result push=: ")

        elif operator == "*":
            print("entered *")
            # result = result * operand
            # number = input("Enter your number: ")
            # operand = float(number)
            # result = result * operand
            # operator = input("Enter operator'+,-,*,/'. For result push=: ")

        elif operator == "/":
            print("entered /")
            # result = result / operand
            # number = input("Enter your number: ")
            # operand = float(number)
            # result = result / operand
            # operator = input("Enter operator'+,-,*,/'. For result push=: ")
        elif operator == "=":
            print("entered =")  # result = operand
            wait_for_end = False
            # print(f" Your result = {result}")
            break

elif operator == "+":
    print("entered +")
    # result = result + operand
    # number = input("Enter your number: ")
    # operand = float(number)
    # result = result + operand
    # operator = input("Enter operator'+,-,*,/'. For result push=: ")

elif operator == "-":
    print("entered -")
    # result = result - operand
    # number = input("Enter your number: ")
    # operand = float(number)
    # result = result - operand
    # operator = input("Enter operator'+,-,*,/'. For result push=: ")

elif operator == "*":
    print("entered *")
    # result = result * operand
    # number = input("Enter your number: ")
    # operand = float(number)
    # result = result * operand
    # operator = input("Enter operator'+,-,*,/'. For result push=: ")

elif operator == "/":
    print("entered /")
    # result = result / operand
    # number = input("Enter your number: ")
    # operand = float(number)
    # result = result / operand
    # operator = input("Enter operator'+,-,*,/'. For result push=: ")

elif operator == "=":
    print("entered =")  # result = operand
    wait_for_end = False
    # print(f" Your result = {result}")
    # break
