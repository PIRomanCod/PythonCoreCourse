from pathlib import Path

message = "Привіт світ! Hello word!"
print(message.encode())
print(message.encode("utf-8"))
print(message.encode("utf-16"))
print(message.encode("cp1251"))
