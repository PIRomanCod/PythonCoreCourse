# Сховище з паролем

class KeyStore:
    def __init__(self, name, password):
        self.__password = None
        self.__name = None
        self.__secret = None

        self.name = name
        self.password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 0:
            self.__name = name
        else:
            raise ValueError("імя має мати довжину")

    @property
    def password(self):
        return "Пароль не показуємо"

    @password.setter
    def password(self, value):
        if self.__password is None:
            self.__password = value
        else:
            if self.is_validate():
                self.__password = value

    @property
    def secret(self):
        return self.__secret

    @secret.setter
    def secret(self, value):
        if self.is_validate():
            self.__secret = value

    def is_validate(self):
        p = input("Password: ")
        if self.__password == p:
            print("Ok")
            return True
        else:
            print("Wrong password")
            return False

k_store = KeyStore("Ivan", "123456")
print("Read password")
print(k_store.password)
# k_store.password = "567234"
print("Set secret value")
k_store.secret = "Test"
print("Read secret value")
print(k_store.secret)