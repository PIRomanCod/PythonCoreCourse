def get_recipe(path, search_id):

    with open(path, "r") as fh:
        keys = ["id", "name", "ingredients"]
        cats_list = []
        cats_dict = []

        while True:
            item = fh.readline()
            if len(item) > 0:
                clear_item = item.removesuffix('\n')
                cats_list.extend(clear_item.split(",", 2))
                cats_list[2] = list(cats_list[2].split(","))
                cats_dict.append(dict(zip(keys, cats_list)))
                cats_list.clear()
            if not item:
                break
        for item in cats_dict:
            for key in item.values():
                if search_id == key:
                    print(item)


get_recipe(r"recipe.txt",
           "60b90c3b13067a15887e1ae4")
