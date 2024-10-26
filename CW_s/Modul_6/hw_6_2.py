
def write_employees_to_file(employee_list, path):

    fh = open(path, 'w')
    line = []
    for sets in employee_list:
        for item in sets:
            item += "\n"
            fh.write(item)

    fh.close()


write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], [
                        'Drake Mikelsson,19']], r"C:\Python\Go_IT\Lessons\Modul_6\employee_list.txt")
#print(pathlib.Path(sys.argv[0]).parent / 'salary.txt')
