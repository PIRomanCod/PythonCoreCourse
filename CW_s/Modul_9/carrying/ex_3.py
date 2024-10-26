from functools import partial

def greeting_simple(msg, name):
    return f"{name} - {msg}"

msg_for_ivan = partial(greeting_simple, name="Ivan")
print(msg_for_ivan("Go to home"))


