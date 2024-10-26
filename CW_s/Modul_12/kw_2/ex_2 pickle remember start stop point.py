import pickle

class TextReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, encoding="utf-8")
        self.line_count = 0

    def custom_file_readline(self):
        self.line_count += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith("\n"):
            line = line[:-1]
        return f"{self.line_count}: {line}"  # ідентичне старому запису. return "%i: %s" % (self.line_count, line)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["file"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)  # відновлюємо атрибути екземпляра (імʼя файлу, та номер рядка)
        # Відновити стан потрібно раніше відриття файлу
        file = open(self.filename, encoding="utf-8")
        for _ in range(self.line_count):
            file.readline()
        self.file = file

if __name__ == "__main__":
    reader = TextReader('line.txt')
    print(reader.custom_file_readline())
    print(reader.custom_file_readline())

    new_reader = pickle.loads(pickle.dumps(reader))  # повинен запамятати коли він був упакований
    # і продовжити друкувати результат з того самого місця

    while True:
        line = new_reader.custom_file_readline()
        if line is None:
            break
        else:
            print(line)

    print('-' * 10)
    print(reader.custom_file_readline())
    print(reader.custom_file_readline())