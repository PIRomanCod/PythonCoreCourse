from collections import UserDict


class Field():
    def __init__(self, name):
        self.value = name


class AdressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record


class Name(Field):
    pass


class Phone(Field):
    pass


class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, old_phone, new_phone):
        print(old_phone)
        for phone in self.phones:
            if old_phone in phone.value:
                self.add_phone(new_phone)
                self.phones.remove(phone)
                return True

    def delete_phone(self, new_phone):
        for phone in self.phones:
            if new_phone in phone.value:
                self.phones.remove(phone)
                return True


CONTACTS_DICT = AdressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            print('\n\nInvalid request entered! Enter the command in the format: \n\n"add Bill 380991112233" or enter "hello"\n')

    return wrapper


def hello():
    commands = {
        '"add"': 'Add new contact',
        '"change"': 'Add a number to an existing contact',
        '"phone"': 'Show contact number',
        '"show all"': 'Show all contacts',
        '"good bye/close/exit"': "Exit",
        '"delete"': '"Deleting contacts"',
        '"hello/help"': 'manual'
    }
    result = f'\n   How can I help you?\n'
    for k, v in commands.items():
        result += '| {:<25} - {:<35} |\n'.format(k, v)

    return result


def add(data):
    name = data.pop(0).title()
    user = Record(name)
    user.add_phone(data)
    CONTACTS_DICT.add_record(user)
    return f'| Contact created!\n| Name: {name}\n| Phone: {data}'


def change(data):
    name = data.pop(0).title()
    phone = data.pop()
    old_number = input('What number to replace? ')
    record_change = CONTACTS_DICT.data[name]

    if record_change.change_phone(old_phone=old_number, new_phone=phone) is True:
        return f'| Contact "{name}" updated: {old_number} ---> {phone}'

    else:
        return '\nThat name is not on the list!'


def delete(data):
    name = data.pop(0).title()
    old_number = input('What number to replace? ')
    record_delete = CONTACTS_DICT.data[name]

    if record_delete.delete_phone(old_number) is True:
        return f'|\n|   Contact: {name} phone: {old_number} ---> deleted.'

    else:
        return 'The phone number not exist'


def phone(name):
    name = str(name).title()
    user = CONTACTS_DICT[name]
    if name in CONTACTS_DICT:
        return '|\n| Name:    {:<15} \n| Phone:   {}\n|'.format(
            name, list(map(lambda x: x.value, user.phones)))
    else:
        return '\nThat name is not on the list!'


def show_all():
    result = '|\n'
    for k, v in CONTACTS_DICT.items():
        result += '|   {:<10}:{}\n'.format(k,
                                           list(map(lambda x: x.value, v.phones)))
    result += '|\n'
    return result


def close_bot():
    return 'Good bye!'


COMMANDS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show_all': show_all,
    'good_bye': close_bot,
    'close': close_bot,
    'exit': close_bot,
    'delete': delete
}


def parser_commands(user_request):
    split_req = user_request.split(' ')
    if len(split_req) == 1:
        for k, v in COMMANDS.items():
            if split_req[0] == k:
                return [v]
    if len(split_req) == 2:
        if split_req[0] == 'show':
            if split_req[1] == 'all':
                return parser_commands('show_all')

    if split_req[0] == 'good':
        if split_req[1] == 'bye':
            return parser_commands('good_bye')

    if split_req[0] == 'phone':
        return [phone, split_req[1]]

    if len(split_req) >= 3:
        command = split_req.pop(0)
        request = split_req
        for k, v in COMMANDS.items():
            if command == k:
                return [v, request]


@input_error
def main():
    while True:

        user_request = input('\nEnter your request or type "hello": ').lower()
        user_request = parser_commands(user_request)

        if len(user_request) == 1:
            command = user_request[0]
            print(command())
            if command == close_bot:
                break

            continue

        if len(user_request) == 2:
            command = user_request[0]
            user_request = user_request[1]
            print(command(user_request))
            continue


if __name__ == '__main__':
    main()
