string = 'ndfjf6cf34fhf 5 5f h2jg33 ff! k'
# new_list = [char for char in string if char.isdigit()]
new_list = [item for item in string if item.isdigit()]
new_list = [item for item in string if '0' <= item <= '9']
print(new_list)

# Заповнити список числами які кратні 30 або 31 в діапазоні 20..250
new_list4 = [item for item in range(20, 250) if item % 30 == 0 or item % 31 == 0]
print(new_list4)