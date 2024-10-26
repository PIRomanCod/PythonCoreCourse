import re


def find_all_links(text):
    result = []
    iterator = re.finditer(
        r"((http|https)\:\/\/)(\w+[.]\w+|\w+)\.([a-zA-Z]){2,6}", text)
    for match in iterator:
        result.append(match.group())
    return result


print(find_all_links("""The main search site in the world is https://www.google.com 
The main social network for people in the world is https://www.facebook.com 
But programmers have their own social network http://github.com 
There they share their code. some url to check https://www..facebook.com www.facebook.com """))


['https://www.google.com', 'https://www.facebook.com', 'http://github.com']
['https://www.google.com', 'https://www.facebook.com', 'https://www..facebook.com']
