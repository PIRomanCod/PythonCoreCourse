"""
LIFO (англ. last in, first out, "останнім прийшов - першим пішов") - спосіб організації даних або іншими словами
Стек (Stack). У структурованому лінійному списку, організованому за принципом LIFO,
елементи можуть додаватися та вибиратися з одного кінця, званого «вершиною списку».
"""

from collections import deque
MAX_LEN = 10
lifo = deque(maxlen=MAX_LEN)

def push(element):
    lifo.appendleft(element)

def pop():
    lifo.popleft()

push("Volodymyr")
push("Ivan")
push("Petro")
push("Iryna")
print(lifo)

name = pop()

print(name)
print(lifo)
