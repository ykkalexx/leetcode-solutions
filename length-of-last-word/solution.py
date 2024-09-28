s = "Hello World Test"
def lengthOfLastWord(s):
    words = s.split()
    number = 0
    for i in enumerate(words[-1]):
        number += 1
    
    print(number)
    return number

lengthOfLastWord(s)