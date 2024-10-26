import re


def is_spam_words(text, spam_words, space_around=False):

    for spam in spam_words:
        text = text.lower()

        if space_around == False:
            dirty = re.findall(spam, text)
            if dirty == None:
                return False
            else:
                return True
        if space_around == True:
            dirty = re.findall(spam, text)
            dirty_0 = re.search(spam, text)
            dirty_1 = re.findall(spam + " ", text)
            dirty_2 = re.findall(" " + spam, text)
            dirty_3 = re.findall(" " + spam + " ", text)
            print(
                f"dirty_0= {dirty_0} dirty = {dirty}, dirty_1= {dirty_1}, dirty_2= {dirty_2}, dirty_3= {dirty_3}")
            if dirty_0 != None and dirty == None and dirty_1 == None and dirty_2 == None and dirty_3 == None:
                return False
            else:
                return True


print(is_spam_words('Ты хорош, но выглядишь как лох.', ['лох'], True))
