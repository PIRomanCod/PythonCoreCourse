def add_employee_to_file(record, path):

    fh = open(path, "a")
    fh.write("\n")
    fh.write(record)
    fh.close()


add_employee_to_file("Drake Mikelsson,19",
                     r"C:\Python\Go_IT\Lessons\Modul_6\employee_list.txt")
