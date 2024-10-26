

# import pathlib
import sys
import shutil
import re
from pathlib import Path

file_extension = {"images": ['JPEG', 'PNG', 'JPG', 'SVG'],
                  "documents": ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
                  "audio": ['MP3', 'OGG', 'WAV', 'AMR'],
                  "video": ['AVI', 'MP4', 'MOV', 'MKV'],
                  "archives": ['ZIP', 'GZ', 'TAR'],
                  "unknown": []
                  }

file_dict = {"images": [],
             "documents": [],
             "audio": [],
             "video": [],
             "archives": [],
             "unknown": []
             }

dir_list = []
files_list = []
untouchible_folder_list = []
# Для того, чтобы получить расширение файла, необходимо использовать свойство .suffix
# или .suffixes (при наличии двойного расширения, например .tar.gz):


def sort(files_list):
    for file in files_list:
        file_ext = Path(file).suffix
        old_place = Path(file)
        new_place = untouchible_folder_list[0]+"/"+normalize(Path(file).name)
        print(old_place, new_place, untouchible_folder_list[0], file_ext.upper(),
              file_extension["images"])
        # if file_ext.upper() in file_extension["images"]:
        #new_place = untouchible_folder_list[0]/normalize(Path(file).name)
        # print(old_place, new_place, file_ext.upper(),
        #      file_extension["images"])
        #shutil.move(old_place, new_place)

        # if file_ext.upper() in file_extension["documents"]:
        #     shutil.move(
        #         Path(file), untouchible_folder_list[1]/normalize(Path(file).name))
        # if file_ext.upper() in file_extension["audio"]:
        #     shutil.move(
        #         Path(file), untouchible_folder_list[2]/normalize(Path(file).name))
        # if file_ext.upper() in file_extension["video"]:
        #     shutil.move(
        #         Path(file), untouchible_folder_list[3]/normalize(Path(file).name))
        # if file_ext.upper() in file_extension["archives"]:
        #     shutil.move(
        #         Path(file), untouchible_folder_list[4]/normalize(Path(file).name))
        # else:
        #     shutil.move(
        #         Path(file), untouchible_folder_list[5]/normalize(Path(file).name))

        # def images_files(name):
        #     pass

        # def documents_files(name):
        #     pass

        # def audio_files(name):
        #     pass

        # def video_files(name):
        #     pass

        # def archives_files(name):
        #     pass

        # def unknown_files(name):
        #     pass


def normalize(files_list):

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    CYRILLIC_SYMBOLS = tuple(CYRILLIC_SYMBOLS)
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}
    normalized_list = []

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    for file_name in files_list:
        translated_name = ""
        file_name = Path(file_name)

        for ch in file_name.name:
            ch = ch.translate(TRANS)
            translated_name = translated_name + ch
        normalized_name = re.sub(r"[^a-zA-Z0-9.]", "_", translated_name)
        normalized_list.append(normalized_name)

    return normalized_list


def recursive_search(path, files_list, dir_list):
    # global dir_list
    # global files_list
    if path.is_dir():
        for element in path.iterdir():
            if element in untouchible_folder_list:
                # print(element)
                continue
            if not element.is_dir():
                # files_list.append(str(element.name))
                files_list.append(str(element))
            if element.is_dir():
                # dir_list.append(str(element.name))
                dir_list.append(str(element))
                recursive_search(element, files_list, dir_list)

    # print(f"dir_list = {dir_list}", len(dir_list))
    # print(f"files_list = {files_list}", len(files_list))
    # return dir_list, files_list


# print(f"dir_list = {dir_list}", len(dir_list))
# print(f"files_list = {files_list}", len(files_list))


def create_folders(path, untouchible_folder_list):
    #global untouchible_folder_list
    for key in file_extension:
        step = Path(path / key)
        if not step.is_dir():
            step.mkdir(parents=True, exist_ok=True)
            untouchible_folder_list.append(str(step))


def main():
    path = r"C:\Users\Professional\Desktop\wastes"
    # path = sys.argv[1]
    path = Path(path)
    # path = pathlib.Path(path) #or perviosly string
    # print(path)
    create_folders(path, untouchible_folder_list)
    recursive_search(path, files_list, dir_list)

    # print(files_list)
    # print(dir_list)
    # print(file_dict)
    # print(untouchible_folder_list)
    sort(files_list)
    # return path


if __name__ == '__main__':
    main()
