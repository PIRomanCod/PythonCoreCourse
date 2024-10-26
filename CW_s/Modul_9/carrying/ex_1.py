# Каррінг - це перетворення функції від багатьох аргументів на набір функцій,
# кожна з яких є функцією від одного аргументу. Ми можемо передати частину аргументів
# у функцію та отримати назад функцію, чекає на інші аргументи.


# В нас є функція, яка приймає 2 параметра name, msg і за допомогою карринга ми розбиваємо на декілька ф-цій
# з одним параметром (код нижче) def greeting(name)

def greeting_simple(name, msg, value):
   return f"{name} - {msg}: {value}"

print(greeting_simple("Ivan", "Go to work!", "55"))
print(greeting_simple("Ivan", "Go to home!", "55"))


def greeting(name):  # Зовнішня ф-ція
   def message(msg):  # Внутрішня ф-ція
      def inner_second(value):
         return f"{name} - {msg}: {value}"
      return inner_second
   return message


msg_for_oksana = greeting("Oksana")  # msg_for_oksana матиме доступ до name через замикання
total_msg = msg_for_oksana("Go to work!")
print(total_msg("55"))