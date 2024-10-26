# str1 = "London-is-a-capital-of-Great-Britain"
# new_str = str1.split("-")
# print(new_str)

# for item in new_str:
#     print(item)

# list1 = ["Alisa", "Bob", "", "Mike", None, "Caroline"]
# list2 = []
# for item in list1:
#     if item:
#         list2.append(item)
# print(list2)

# str2 = "Alisa18 is a student2 2in course4 and learn"

# res = []

# temp = str2.split()
# print(temp)

# for item in temp:
#     if any(ch.isalpha() for ch in item) and any(ch.isdigit() for ch in item):
#         res.append(item)

# print(res)


# import string

# str3 = "/^Alisa is @python developer & ruby *dev"

# replaced_char = "#"

# for char in string.punctuation:
#     str3 = str3.replace(char, replaced_char)
# print(str3)

new_dict = {
    "name": "Alisa",
    "age": 22,
    "salary": 1000,
    "position": "developer"
}
# long
keys_extract = ["name", "salary"]

res_dict = {}

for key in keys_extract:
    res_dict.update({key: new_dict[key]})

print(res_dict)

# short
res_dict2 = {k: new_dict[k] for k in keys_extract}

print(res_dict2)
