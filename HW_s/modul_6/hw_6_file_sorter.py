import sys
import shutil
import re
from pathlib import Path

file_extension = {"images": ['.jpeg', '.png', '.jpg', '.svg'],
                  "documents": ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
                  "audio": ['.mp3', '.ogg', '.wav', '.amr'],
                  "video": ['.avi', '.mp4', '.mov', '.mkv'],
                  "archives": ['.zip', '.gz', '.tar'],
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


def sort(files_list, path, file_dict, file_extension):
    for file in files_list:
        file_ext = Path(file).suffix
        file_stem = Path(file).stem
        new_file_stem = normalize(file_stem)+file_ext
        old_place = Path(file)

        if file_ext.lower() in file_extension["images"]:
            new_place = path / "images" / new_file_stem
            file_dict["images"].append(new_file_stem)
            shutil.move(old_place, new_place)

        elif file_ext.lower() in file_extension["documents"]:
            new_place = path / "documents" / new_file_stem
            file_dict["documents"].append(new_file_stem)
            shutil.move(old_place, new_place)

        elif file_ext.lower() in file_extension["audio"]:
            new_place = path / "audio" / new_file_stem
            file_dict["audio"].append(new_file_stem)
            shutil.move(old_place, new_place)

        elif file_ext.lower() in file_extension["video"]:
            new_place = path / "video" / new_file_stem
            file_dict["video"].append(new_file_stem)
            shutil.move(old_place, new_place)

        elif file_ext.lower() in file_extension["archives"]:
            new_place = path / "archives" / new_file_stem
            file_dict["archives"].append(new_file_stem)
            shutil.move(old_place, new_place)
            shutil.unpack_archive(new_place, path / "archives"/file_stem)

        else:
            new_place = path / "unknown" / new_file_stem
            file_dict["unknown"].append(new_file_stem)
            file_extension["unknown"].append(file_ext)
            shutil.move(old_place, new_place)


def normalize(file_stem):

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    CYRILLIC_SYMBOLS = tuple(CYRILLIC_SYMBOLS)
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    translated_name = ""
    for ch in file_stem:
        ch = ch.translate(TRANS)
        translated_name = translated_name + ch
    normalized_name = re.sub(r"[^a-zA-Z0-9.]", "_", translated_name)

    return normalized_name


def recursive_search(path, files_list, dir_list):
    if path.is_dir():
        for element in path.iterdir():
            if element in untouchible_folder_list:
                continue
            if element.is_file():
                files_list.append(str(element))
            elif element.is_dir():
                dir_list.append(str(element))
                recursive_search(element, files_list, dir_list)
    return dir_list


def create_folders(path, untouchible_folder_list):
    for key in file_extension:
        step = Path(path / key)
        if not step.is_dir():
            step.mkdir(parents=True, exist_ok=True)
            untouchible_folder_list.append(step)
    return untouchible_folder_list


def clear_folders(dir_list, untouchible_folder_list):
    for element in dir_list[::-1]:
        if element not in untouchible_folder_list:
            Path(element).rmdir()


def main():
    try:
        path = sys.argv[1]
    except IndexError:
        print("\nYou have to write full folder name for sorting after script name!!!\nTry again please.\n")
    else:
        path = Path(path)
        create_folders(path, untouchible_folder_list)
        recursive_search(path, files_list, dir_list)
        sort(files_list, path, file_dict, file_extension)
        clear_folders(dir_list, untouchible_folder_list)
        print(
            f"file_dict  =   {file_dict},\n file_extension   =    {file_extension}")


if __name__ == '__main__':
    main()
