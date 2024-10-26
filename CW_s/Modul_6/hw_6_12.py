import base64

data = ['andry:uyro18890D', 'steve:oppjM13LL9e']


def encode_data_to_base64(data):
    list = []
    for item in data:
        message_bytes = item.encode("utf-8")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("utf-8")
        list.append(base64_message)
    return list


encode_data_to_base64(data)
