import pickle

d = {'some key': 12345}

with open('my_dict.bin', 'wb') as file:
    pickle.dump(d, file)  # записуємо серіалізований обєкт у файл

d_bytes = pickle.dumps(d)
print(d_bytes)