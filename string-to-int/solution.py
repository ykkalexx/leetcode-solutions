s = "0-1"
#output = 133
# if the next character is a letter, then the number is finished
# this question is so SO SO bad
# all the edge cases are really stupid
# this works 
# but not for all edge cases


def stringToInt(s):
    num = 0
    n = ""
    symbol = ""
    news = s.strip()
    for i in news:
        if i.isnumeric():
            n = n + i
            num = int(n)
            continue
        elif i == "-":
            symbol = "-"
            continue
        elif i == 0:
            continue
        else:
            break
    if symbol:
        add = str(symbol) + str(num)
        result = int(add)
        return result
    return num

print(stringToInt(s))