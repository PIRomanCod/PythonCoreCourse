# module 7 - 5

def capital_text(s: str) -> str:
    s = s.capitalize()
    b = s.split(' ')
    index = 0
    while index < len(b):
        if b[index][-1] in ('?', '!', '.') and index+1 < len(b):
            b[index+1] = b[index+1].capitalize()
        index += 1
    return ' '.join(b)
