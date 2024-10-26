# module 7 - 8

def token_parser(s):
    s = s.replace(" ", "")
    tokens = []
    i = 0
    while i < len(s):
        if (
            s[i] == "*"
            or s[i] == "/"
            or s[i] == "("
            or s[i] == ")"
            or s[i] == "+"
            or s[i] == "-"
        ):
            tokens.append(s[i])
            i += 1
        elif "0" <= s[i] <= "9":
            num = ''
            while i < len(s) and "0" <= s[i] <= "9":
                num = num + s[i]
                i += 1
            tokens.append(num)
        else:
            i += 1
    return tokens
