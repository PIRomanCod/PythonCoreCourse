from copy import deepcopy, copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_obj = Person(self.name, self.email, self.phone, self.favorite)
        copy_obj.name = copy(self.name)
        copy_obj.email = copy(self.email)
        copy_obj.phone = copy(self.phone)
        copy_obj.favorite = copy(self.favorite)
        return copy_obj


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_obj = Contacts(None, None)
        copy_obj.filename = copy(self.filename)
        copy_obj.contacts = copy(self.contacts)
        copy_obj.is_unpacking = copy(self.is_unpacking)
        copy_obj.count_save = copy(self.count_save)
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Contacts(None, None)
        memo[id(copy_obj)] = copy_obj
        copy_obj.filename = deepcopy(self.filename)
        copy_obj.contacts = deepcopy(self.contacts)
        copy_obj.is_unpacking = deepcopy(self.is_unpacking)
        copy_obj.count_save = deepcopy(self.count_save)
        return copy_obj


contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),


]

filename = "user_class.dat"
persons = Contacts("user_class.bin", contacts)
# print(persons, type(persons))
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[1] == person_from_file.contacts[1])  # False
print(persons.contacts[1].name == person_from_file.contacts[1].name)
# True
print(persons.contacts[1].email == person_from_file.contacts[1].email)
# True
# True
print(persons.contacts[1].phone == person_from_file.contacts[1].phone)  # True
persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True
new_persons = copy(persons)
deep_new_persons = deepcopy(persons)

#new_persons.contacts[0].name = "Another name"

print(persons)  # Allen Raymond
print(new_persons)  # Another name
print(deep_new_persons)
