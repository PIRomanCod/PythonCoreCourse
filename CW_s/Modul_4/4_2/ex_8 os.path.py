import os
print(os.path.join('usr', 'bin', 'media'))

print(os.getcwd())

# os.makedirs('test')

print(os.path.abspath("ex_1.py"))
print(os.path.isabs("ex_1.py"))
os.path.relpath(path='C:\\Windows', start="C:\\")