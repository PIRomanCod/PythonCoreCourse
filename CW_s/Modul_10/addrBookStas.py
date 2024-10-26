from collections import UserDict
from datetime import datetime
import pickle


class Field:
    def __init__(self, value: str):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):

    @Field.value.setter
    def value(self, name: str):
        if name.isnumeric():
            raise ValueError('Wrong name')
        self._value = name


class Phone(Field):

    @Field.value.setter
    def value(self, phone: str):
        if not phone.isnumeric():
            raise ValueError('Wrong phones')
        format_phone = self.format_phone_number(phone)
        if format_phone:
            self._value = format_phone

    @staticmethod
    def format_phone_number(phone: str):
        if len(phone) == 10:
            return f'+38{phone}'
        elif len(phone) == 12:
            return f'+{phone}'
        else:
            raise ValueError('Wrong phones')


class Birthday(Field):

    @Field.value.setter
    def value(self, birthday: str):
        current_date = datetime.now().date()
        birthday_date = datetime.strptime(birthday, '%Y-%m-%d').date()
        if birthday_date > current_date:
            raise ValueError("Your contact havent born yet")
        self._value = birthday


class Record:

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def get_info(self):
        birthday_info = ''
        phones_info = [phone.value for phone in self.phones]

        if self.birthday:
            birthday_info = f' Birthday: {self.birthday.value}'

        return f'{self.name.value} : {", ".join(phones_info)}{birthday_info}'

    def day_to_bithday(self):
        if not self.birthday:
            raise ValueError('This contact havent birthday date')

        current_date = datetime.now().date()

        birthday_date = datetime.strptime(
            self.birthday.value, '%Y-%m-%d').date()
        this_year_birthday = birthday_date.replace(year=current_date.year)

        if this_year_birthday < current_date:
            this_year_birthday = this_year_birthday.replace(
                year=current_date.year + 1)

        return (this_year_birthday - current_date).days

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def add_birthday(self, date: str):
        self.birthday = Birthday(date)

    def delete_phone(self, phone: str):
        for record_phone in self.phones:
            if record_phone.value == phone:
                self.phones.remove(record_phone)
                return True
        return False

    def change_phone(self, phones):
        for phone in phones:
            if not self.delete_phone(phone):
                self.add_phone(phone)


class AdressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.load_from_file()

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def get_all_record(self):
        return self.data

    def has_record(self, name):
        return bool(self.data.get(name))

    def get_record(self, name) -> Record:
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]

    def search(self, value):
        if self.has_record(value):
            return self.get_record(value)

        for record in self.get_all_record().values():
            for phone in record.phones:
                if phone.value == value:
                    return record

        raise ValueError("Contact with this value does not exist.")

    def iterator(self, count=3):
        result = []

        for contact in self.data.values():
            result.append(contact)
            if len(result) == count:
                yield result
                result = []

        if result:
            yield result

    def save_to_file(self):
        with open('AdressBook.bin', 'wb') as fw:
            pickle.dump(self.data, fw)

    def load_from_file(self):
        try:
            with open('AdressBook.bin', 'rb') as fr:
                self.data = pickle.load(fr)
        except FileNotFoundError:
            pass


CONTACTS = AdressBook()


def get_help():
    return '''Command to execute: 
>>> hello
>>> help - show commands list
>>> add - add new contact in storage Example: add "name (only letters without spaces)" "phone number (only digits without spaces)"
>>> change - change existing contact Example: chnage "exist contact name (only letters without spaces)" "new phone number (only digits without spaces)"
>>> phone - show exist contact name and phone
>>> show all - show all existing contacts
>>> delete phone - remove entered phone from contact Example: delete phone "name (only letters without spaces)" "phone number (only digits without spaces)"
>>> delete - remove contact Example: delete "name (only letters without spaces)" 
>>> good bye/close/exit - bye bye
>>> birthday - add birthday date to the contact Example: bithday name date(yyyy-mm-dd)
>>> days to birthday - show how much days left to the contact birthday Example: days to birthday name\n'''


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except KeyError:
            return 'This contact doesnt exist, please try again.'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'This contac cannot be added, it exists already'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'

    return inner


def greeting():
    return 'How can I help you?'


def stop_bot():
    return 'Good bye!'


def add_contact(data):

    name, phones = get_data_from_user(data)

    if name in CONTACTS:
        raise ValueError('This contact already exist.')

    record = Record(name)

    for phone in phones:
        record.add_phone(phone)

    CONTACTS.add_record(record)

    return f'contact {name} was added'


def change_contact(data):

    name, phones = get_data_from_user(data)
    record = CONTACTS[name]
    record.change_phone(phones)

    return 'Contact was updated'


def show_contact_phone(data: str):
    return CONTACTS.search(data.strip()).get_info()


def show_all_contacts():

    result = [record.get_info() for page in CONTACTS.iterator()
              for record in page]
    return '\n'.join(result)


def del_phone(data):
    name, phone = data.strip().split(' ')

    record = CONTACTS[name]
    if record.delete_phone(phone):
        return f'Phone {phone} for {name} contact deleted.'
    return f'{name} contact does not have this number'


def del_contact(data):
    CONTACTS.remove_record(data.strip())
    return 'Contact was deleted'


def add_birth(data):
    name, birthday = data.strip().split(' ')
    record = CONTACTS[name]
    record.add_birthday(birthday)
    return f'For {name} you add Birthday {birthday}'


def days_to_birthday(data: str):
    record = CONTACTS[data.strip()]
    return record.day_to_bithday()


COMMANDS = {'hello': greeting,
            'help': get_help,
            'add': add_contact,
            'change': change_contact,
            'phone': show_contact_phone,
            'show all': show_all_contacts,
            'good bye': stop_bot,
            'close': stop_bot,
            'exit': stop_bot,
            'delete phone': del_phone,
            'delete': del_contact,
            'birthday': add_birth,
            'days to birthday': days_to_birthday}


def break_func():
    return 'Wrong enter'


def get_data_from_user(data: str):
    name, *phones = data.lower().strip().split(' ')

    return name, phones


def get_command(command):
    return COMMANDS.get(command, break_func)


@input_error
def get_user_request(user_input: str):
    command = ''
    data = ''

    for key in COMMANDS:
        if user_input.strip().lower().startswith(key):
            command = key
            data = user_input[len(key):]
            break

    if data:
        return get_command(command)(data)
    return get_command(command)()


def main():
    try:

        print(get_help())
        while True:

            user_request = input('Wait for your command master: ')
            result = get_user_request(user_request)
            print(result)

            if result == 'Good bye!':
                break
    finally:
        CONTACTS.save_to_file()


if __name__ == '__main__':

    main()
