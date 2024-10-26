def save_credentials_users(path):  # users_info
    users_info = {'andry': 'uyro18890D',
                  'steve': 'oppjM13LL9e'}  # username:password
    my_list = []
    for key, value in users_info.items():
        my_list.append("{}:{}".format(key, value))

    print(my_list)

    with open(path, 'wb') as fh:
        for item in my_list:
            item += "\n"
            item = bytes(item, 'utf-8')
            fh.write(item)


save_credentials_users(r"credentials_users.bin")
