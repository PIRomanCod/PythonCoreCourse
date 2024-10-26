

def get_cats_info(path):

    with open(path, "r") as fh:

        lines = ["id", "name", "age"]
        cats_list = []
        cats_dict = []
        while True:
            item = fh.readline()
            if len(item) > 0:
                clear_item = item.removesuffix('\n')
                cats_list.extend(clear_item.split(","))
                cats_dict.append(dict(zip(lines, cats_list)))
                cats_list.clear()
            if not item:
                break
        return cats_dict


get_cats_info(r"C:\Python\Go_IT\Lessons\Modul_6\cats_info.txt")
