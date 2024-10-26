# Замикання

# Особливість існування вкладених локальних просторів імен і той факт, що вони створюються динамічно,
# дає можливість використати механізм замикань у Python.

def greeting(name):  # Зовнішня ф-ція
    def message(msg):  # Внутрішня ф-ція
        return f"{name} - {msg}"
    return message

msg_for_ivan = greeting("Ivan")  # msg_for_ivan матиме доступ до name через замикання
msg_for_oksana = greeting("Oksana")  # msg_for_oksana матиме доступ до name через замикання

print(msg_for_ivan("Go to home!"))
print(msg_for_ivan("Go to work!"))


print(msg_for_oksana("Good job!"))
print(msg_for_oksana("have a nice day"))

