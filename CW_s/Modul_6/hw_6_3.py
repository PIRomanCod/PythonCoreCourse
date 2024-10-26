

def read_employees_from_file(path):

    fh = open(path, "r")
    line = []
    while True:
        item = fh.readline()
        middle_clear = item.split(",")
        #clear_item = re.findall(r"\d{1,}", middle_clear)
        # line.extend(clear_item)
        if not item:
            break
    fh.close()
    print(item, line, middle_clear)


read_employees_from_file(r"C:\Python\Go_IT\Lessons\Modul_6\employee_list.txt")
