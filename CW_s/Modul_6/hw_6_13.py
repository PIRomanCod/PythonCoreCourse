import base64
import shutil

employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}


def create_backup(path, file_name, employee_residence):
    my_list = []
    for key, value in employee_residence.items():
        my_list.append("{} {}".format(key, value))

    print(my_list)

    with open(path + '/' + "employee_residence.bin", 'wb') as fh:
        for item in my_list:
            item += "\n"
            #item = bytes(item, 'utf-8')
            message_bytes = item.encode("utf-8")
            base64_bytes = base64.b64encode(message_bytes)
            #base64_message = base64_bytes.decode("utf-8")
            fh.write(base64_bytes)

    archive_name = shutil.make_archive(
        'backup_folder', 'zip', path)

    return archive_name


create_backup(r"C:\Python\Go_IT\Lessons\Modul_6\ ",
              "employee_residence.bin", employee_residence)
