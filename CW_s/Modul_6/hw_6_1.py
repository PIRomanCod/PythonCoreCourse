import re


def total_salary(path):

    fh = open(path, 'r')
    all_file = fh.read()
    nums = re.findall("\d{1,}", all_file)
    total = float(sum(int(item) for item in nums))
    fh.close()

    return total


print(total_salary(r"C:\Python\Go_IT\Lessons\Modul_6\salary.txt"))
#print(pathlib.Path(sys.argv[0]).parent / 'salary.txt')
