from pathlib import *

current_dir = Path.cwd()
home_dir = Path.home()

print(current_dir)
print(home_dir)

# import os
#
# outhpath = os.path.join(os.getcwd(), 'output')
# outhpath_file = os.path.join(outhpath, 'new_file.txt')

outhpath = Path.cwd() / 'output' / 'new_file.txt'
print(outhpath)

a = Path('directory', 'new.txt')
print(a)
print(a.name)
print(a.suffix)
