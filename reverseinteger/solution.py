x = -123

def reverseInt(x):
    num = str(x)
    if x < 0:
        num = num[1:]
        return int("-" + num[::-1])
    else:
       return int(num[::-1])

print(reverseInt(x))