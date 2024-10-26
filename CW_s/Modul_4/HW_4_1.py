def format_ingredients(items):

    value = len(items)
    if value == 0:
        last_item = items
        return last_item

    elif value == 1:
        last_item = items[0]
        return last_item

    elif value == 2:
        last_item = items.pop(-1)
        prelast_item = items.pop(-1)
        new_last_item = (prelast_item + " and " + last_item)
        return new_last_item

    else:
        last_item = items.pop(-1)
        prelast_item = items.pop(-1)
        new_last_item = (prelast_item + " and " + last_item)
        count = len(items)
        string = "_"

        for count in items:
            string = string + ", " + count

        string = string + ", " + new_last_item
        string_copy = string[3::]
        return string_copy


print(format_ingredients(
    []))
