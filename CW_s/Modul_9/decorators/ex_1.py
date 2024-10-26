# Декоратори

# Шаблон проектування, який полягає в тому, щоб розширювати існуючий функціонал,
# не вносячи змін у код цього самого функціоналу.

def greeting(name):
    print(f"My name is {name}")


def greeting_decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello")
        result = func(*args, **kwargs)
        print("Have a nice day")
        return result
    return wrapper


greeting("Ivan")
# ==================
change_greeting = greeting_decorator(greeting)
change_greeting("Ivan")
