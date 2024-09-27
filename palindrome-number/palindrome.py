# palindrome means a number is same from left to right and right to left
def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else 
        return False