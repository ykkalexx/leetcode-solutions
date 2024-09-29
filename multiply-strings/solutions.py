# Note: this stupid questiom doesn't make sense and it's forcing people to use\
# the stupidest things that are error prone to solve it.
# i solved the normal human being way
# be for real?

num1 = "123"
num2 = "456"

def multiplyStrings(num1, num2):
    number1 = int(num1)
    number2 = int(num2)
    result = number1 * number2
    str_result = str(result)

    return str_result

print(multiplyStrings(num1, num2))