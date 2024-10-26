'''ДЗ 9:
CLI (Command Line Interface)
3 частини:
-Парсер команд.
-Функції обробники команд — набір функцій, які ще називають handler
-Цикл запит-відповідь. Ця частина програми відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції-handlerа
Функціонал:
- бот-асистент повинен вміти зберігати ім'я та номер телефону,
- знаходити номер телефону за ім'ям,
- змінювати записаний номер телефону,
- виводити в консоль всі записи, які зберіг
Всі помилки введення повинні оброблятися за допомогою декоратора input_error, повідомлення користувачеві про помилки

Додаткове розширення у ДЗ 10:
В цій домашній роботі ви повинні реалізувати такі класи:
-Клас AddressBook, який успадковується від UserDict, та ми потім додамо логіку пошуку за записами до цього класу.
-Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name.
-Клас Field, який буде батьківським для всіх полів, у ньому потім реалізуємо логіку загальну для всіх полів.
-Клас Name, обов'язкове поле з ім'ям.
-Клас Phone, необов'язкове поле з телефоном та таких один запис (Record) може містити кілька.
- Реалізовано всі класи із завдання.
- Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value.
- Record зберігає об'єкт Name в окремому атрибуті.
- Record зберігає список об'єктів Phone в окремому атрибуті.
- Record реалізує методи для додавання/видалення/редагування об'єктів Phone.
- AddressBook реалізує метод add_record, який додає Record у self.data.'''

from collections import UserDict


class VerificationError(Exception):
    pass


class OwnerError(Exception):
    pass


class NoUserError(Exception):
    pass


class Field:
    def __init__(self, name):
        self.value = name


class Name(Field):
    pass


class Phone(Field):
    pass


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_contact(self, name):
        del self.data[name]


class Record(Field):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.add_phone(new_phone)
                self.phones.remove(phone)
                return True

    def delete_phone(self, delete_phone):
        for phone in self.phones:
            if phone.value == delete_phone:
                self.phones.remove(phone)
                return True


def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except (TypeError):
            return "The command don't need args"
        except (IndexError):
            return "The command need 2 args: name phone"
        except (KeyError):
            return "The command is unknown"
        except (VerificationError):
            return "The phone number incorrect, enter please 3 operators + 7 phone digits"
        except (OwnerError):
            return "The phone number is related with other contact"
        except (NoUserError):
            return "AddressBook hasn't the contact name yet, please add before change"
    return inner


def parser(user_input):
    parsed_input = user_input.lower().strip().split()
    return handler(parsed_input)


@input_error
def handler(parsed_input):
    if parsed_input[0] in commands_dict:
        if len(parsed_input) == 1:
            action = commands_dict.get(parsed_input[0])()
        else:
            action = commands_dict.get(parsed_input[0])(
                (" ").join(parsed_input[1:]))

    else:
        raise KeyError
    return action


def hello():
    return f"How can I help you? Enter: 'help' for manual"


def add(string):
    new_elem = string.split()
    if users.data.get(new_elem[0]):
        return "Contact already exist"

    record = Record(new_elem[0])
    record.add_phone(new_elem[1])
    users.add_record(record)
    return f"You added new contact: {new_elem[0]} with phone number: {new_elem[1]}"


def add_phone(string):
    new_elem = string.split()

    if not phone_verification(string):
        raise VerificationError
    else:
        if users.data.get(new_elem[0]):
            record = users.data[new_elem[0]]
            record.add_phone(new_elem[1])
            return f"You added contact {new_elem[0]} with number {new_elem[1]}"
        else:
            return "There is no contact with this name"


def phone_verification(string):
    new_elem = string.split()
    if new_elem[0].isdigit():
        raise IndexError

    if new_elem[1].isdigit() and len(new_elem[1]) == 10:
        return True
    if len(new_elem) == 3:
        if new_elem[2].isdigit() and len(new_elem[2]) == 10:
            return True
    else:
        return False


def change(string):
    new_elem = string.split()
    if new_elem[0] not in users.data.keys():
        raise NoUserError
    elif not phone_verification(string):
        raise VerificationError
    else:
        record = users.data[new_elem[0]]
        if record.change_phone(new_elem[1], new_elem[2]) is True:
            return f"You changed for contact {new_elem[0]} old phone {new_elem[1]} to new phone {new_elem[2]}"
        else:
            return "Phone number does not exist"


def delete_phone(string):
    new_elem = string.split()
    record = users.data[new_elem[0]]

    if record.delete_phone(new_elem[1]) is True:
        return f"For contact {new_elem[0]} phone number: {new_elem[1]} was deleted"
    else:
        return "Phone number does not exist"


def phone(string):
    new_elem = string.split()
    if new_elem[0] in users.data.keys():
        phones_list = []
        for phone in users.data[new_elem[0]].phones:
            phones_list.append(phone.value)
        return f"Contact {new_elem[0]} have next phones: {phones_list}"
    else:
        return f"There is no contact with this name"


def show_all():
    if not users.data:
        return "AddressBook is empty"

    contacts = ""
    for name, record in users.items():
        phones_list = []
        for phone in record.phones:
            phones_list.append(phone.value)
        contacts += f"{name}: {phones_list}\n"
    return contacts


def delete_contact(string):
    new_elem = string.split()
    users.delete_contact(new_elem[0])
    return f"You delete contact {new_elem[0]}"


def exit():
    return "Good bye!"


def manual():
    return '''Please enter one of the commands:
    ">>hello", 
    ">>add_contact 'name' 'number'", 
    ">>add_phone 'name' 'number'", 
    ">>change_phone 'name' 'old_number' 'new_number'",
    ">>search_phone 'name'", 
    ">>delete_phone 'name' 'number'", 
    ">>delete_contact 'name'", 
    ">>show_all", 
    ">>exit", ">>good_bye", ">>close"
    '''


the_end = False

users = AddressBook()

commands_dict = {"hello": hello,
                 "help": manual,
                 "add_contact": add,
                 "add_phone": add_phone,
                 "change_phone": change,
                 "search_phone": phone,
                 "delete_contact": delete_contact,
                 "show_all": show_all,
                 "exit": exit}

commands_list = [">>hello", ">>add_contact 'name' 'number'", ">>add_phone 'name' 'number'", ">>change_phone 'name' 'old_number' 'new_number'",
                 ">>search_phone 'name'", ">>delete_phone 'name' 'number'", ">>delete_contact 'name'", ">>show_all", ">>exit", ">>good_bye", ">>close"]


def main():
    print(hello())
    while not the_end:
        user_input = input("Enter please: ").lower()
        if user_input in ["good_bye", "close", "exit"]:
            print(commands_dict.get("exit")())
            break
        else:
            print(parser(user_input))


if __name__ == '__main__':

    main()
