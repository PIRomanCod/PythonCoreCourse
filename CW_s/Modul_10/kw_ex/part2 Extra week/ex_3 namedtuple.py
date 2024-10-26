# module 8 - 7
import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

def convert_list(cats):
    result = list()
    if isinstance(cats[0], Cat):
        for cat in cats:
            result.append({"nickname": cat.nickname, "age": cat.age, "owner": cat.owner})
        return result
    for cat in cats:
        result.append(Cat(cat.get("nickname"), cat.get("age"), cat.get("owner")))
    return result
