def get_credentials_users(path):
    list = []
    with open(path, 'rb') as fh:

        while True:
            item = fh.readline()
            if len(item) > 0:
                item = item.decode()
                item = item.removesuffix('\n')
                list.append(item)

            if not item:
                break
    print(list)


get_credentials_users(r"credentials_users.bin")
