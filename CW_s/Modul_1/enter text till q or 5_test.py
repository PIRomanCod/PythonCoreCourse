counter = 0

while True:
    user_input = input("Welcome: ")
    counter = counter + 1

    if user_input == "q" or counter >= 5:
        break
    else:
        print(f"You printed: {user_input}")
