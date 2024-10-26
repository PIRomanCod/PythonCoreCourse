import pickle

FILENAME = "users.dat"
users = [
    ['Tom', 18, True],
    ['Alice', 23, True],
    ['Bob', 35, False]
]
with open(FILENAME, 'wb') as file:
    pickle.dump(users, file)

with open(FILENAME, 'rb') as read_file:
    users_from_file = pickle.load(read_file)
    for user in users_from_file:
        print("Name:", user[0], "\tAge:", user[1], "\tStatus(single):", user[2])
