# Написати Contex Manager FileReader, який пише в лог timestamp коли файл був відкритий,
# timestamp, коли файл був закритий, ім'я файлу, і як довго файл був відкритий з точністю до секунд.

from datetime import datetime
from time import sleep


class FileReader:
    def __init__(self, filename):
        self.file = None
        self.opened = False
        self.filename = filename
        self.log = ""
        self.timestamp = None

    def __enter__(self):
        self.file = open(self.filename, "r")
        self.opened = True
        self.timestamp = datetime.now().timestamp()
        msg = "{:<20}|{:^15}| open \n".format(self.timestamp, self.filename)
        self.log += msg
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
            timestamp = datetime.now().timestamp()
            diff = timestamp - self.timestamp
            msg = "{:<20}|{:^15}| closed: {:>15} \n".format(timestamp, self.filename, round(diff, 6))
            self.log += msg
        self.opened = False

reader = FileReader("new_file.txt")

with reader as f:
    sleep(2)
    print(f.read())

with reader as f:
    sleep(1)
    print(f.read())

print(reader.log)