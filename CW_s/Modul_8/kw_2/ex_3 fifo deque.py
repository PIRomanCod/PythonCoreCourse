"""
FIFO (англ. first in, first out - "першим прийшов - першим пішов") - спосіб організації даних або іншими словами черга.
Цей вислів описує принцип технічної обробки черги або обслуговування конфліктних вимог
шляхом упорядкування процесу за принципом: "першим прийшов - першим обслужений". Той, хто приходить першим,
той і обслуговується першим, хто прийде наступним чекає, поки обслуговування першого не буде закінчено, і так далі.
"""

from collections import deque
MAX_LEN = 10
fifo = deque(maxlen=MAX_LEN)

def push(element):
    fifo.append(element)

def pop():
    return fifo.popleft()

push("Volodymyr")
push("Volodymyr")
push("Ivan")
push("Ivan")
push("Ivan")
push("Petro")
push("Petro")
push("Petro")
push("Iryna")
push("Iryna")
push("Iryna")
push("Iryna")
push("Iryna")
push("Iryna")
print(fifo)
a = list(fifo)
print(a)
for item in fifo:
    print(item, end=" * ")
# name = pop()
# print(name)
# print(fifo)
