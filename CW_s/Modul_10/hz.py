from collections import UserDict


class User(UserDict):
    def get_name(self):
        return self.data["name"]

    def add_phone(self, phone):
        phones = self.data.get("phones", [])
        phones.append(phone)
        self.data["phones"] = phones


user = User()
user["name"] = "Bob"
user.add_phone("123456")
user.add_phone("500000")
print(user)
print(user.__dict__)
