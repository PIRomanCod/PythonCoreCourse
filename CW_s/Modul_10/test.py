class Field:
    def __init__(self, value):
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
    def value(self, value):
        if value.isdigit():
            raise ValueError("Name cannot be a numbers")
        self._value = value


class Phone(Field):

    @Field.value.setter
    def value(self, value):
        print(f"i am inside of setter {value}")
        checked_phone = self.phone_verification(value)
        if checked_phone:
            self._value = value

    @staticmethod
    def phone_verification(value):
        if value.isalpha():
            raise IndexError
        if value.isdigit() and len(value) == 10:
            return True
        else:
            return False


phone = Phone("15012345678")
print(phone.value)
phone2 = Phone("dfdsd2gdfdgg")
print(phone2.value)
print(phone2.phone_verification("1501234567"))
print(phone.phone_verification("dfdsd2gdfdgg"))
nnn = Name(123)
print(nnn.value)
