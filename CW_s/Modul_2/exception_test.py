while True:

    age = input("How old are you?: ")
    try:
        age = int(age)

        if age >= 18:
            print("You are adult")

    except ValueError:
        print(f"You entered '{age}' Can be only numbers!!!")
    else:
        break
    finally:
        print("==================\n")
