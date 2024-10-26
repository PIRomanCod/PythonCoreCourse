# import pathlib
import sys
import shutil
import re
from pathlib import Path, WindowsPath


# files_list = ['Pink Floyd - Хей хей Rise Up (feat Andriy Khlyvnyuk of Boombox).mp3',
#               'балага.docx', 'Дайкири - Папа.wav', 'люБИмаЯ.JPG', 'Новая папк0а.zip',
#               'Одария Мальва.jpg', 'пусто.txt']
# files_list = ['C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\konkurs2mp3.sfk', 'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\README.md', 'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка(2)\\TL Ziraatbank 2020_01.tif', 'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка(2)\\TL Ziraat bank 2020_01.zip',
#               'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка(2)\\белье.jpg', 'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка(2)\\Одария Мальва.jpg', 'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка(2)\\Подъём - Кораблики(Dance_Mix).mp3']

files_list = ['C:\\Users\\Professional\\Desktop\\wastes\\вид юшк а2.mp4',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка\\Автокопия Modul_4_hw.asd',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка\\видюшка.mp4',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка\\Документ Microsoft Word.docx',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка\\Новый текстовый документ.txt',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка\\фотка.jpeg',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка\\фотка.zip',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\konkurs2mp3.sfk',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\README.md',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\TL Ziraat bank 2020_01.tif',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\TL Ziraat bank 2020_01.zip',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\белье.jpg',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\Новая папка111\\Pink Floyd - Хей хей Rise Up (feat Andriy Khlyvnyuk of Boombox).mp3',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\Новая папка111\\балага.docx',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\Новая папка111\\Дайкири - Папа.wav',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\Новая папка111\\люБИмаЯ.JPG',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\Новая папка111\\Новая папк0а.zip',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\Новая папка111\\Новая папка33\\123.pptx',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\Новая папка111\\Одария Мальва.jpg',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\Новая папка111\\пусто.txt',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\Одария Мальва.jpg',
              'C:\\Users\\Professional\\Desktop\\wastes\\Новая папка (2)\\Подъём - Кораблики(Dance_Mix).mp3',
              'C:\\Users\\Professional\\Desktop\\wastes\\опять Пусто.docx',
              'C:\\Users\\Professional\\Desktop\\wastes\\пошли со мной.jpg',
              'C:\\Users\\Professional\\Desktop\\wastes\\Снова ФИГНЯ.txt',
              'C:\\Users\\Professional\\Desktop\\wastes\\Снова ФИГНЯ.zip']


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


print(normalize(files_list))
# normalize(files_list)
