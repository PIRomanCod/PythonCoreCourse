import re


def find_word(text, word):

    dict = {"result": False, "first_index": None, "last_index": None}

    search = re.search(word, text)
    if search != None:
        dict["result"] = True

    nums = search.span()
    print(nums, type(nums))
    dict["first_index"] = nums[0]
    dict["last_index"] = nums[1]

    dict["search_string"] = word
    dict["string"] = text

    return dict


print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))
