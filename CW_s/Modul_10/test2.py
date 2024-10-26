class Field:
    def __init__(self, value):
        self._value = None
        self._value = value


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


phone = Phone("1501234567")
print(phone.value)
#phone2 = Phone("dfdsd2gdfdgg")
# print(phone2.value)
# print(phone2.phone_verification("1501234567"))
print(phone.format_phone_number("dfdsd2gdfdgg"))
nnn = Name("123")
print(nnn.value)
