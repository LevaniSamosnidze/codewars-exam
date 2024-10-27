# ) Palindrome Checker (3 ქულა)
# Create a program that checks if a given string is a palindrome
#  (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.

# Examples:

# "A man a plan a canal Panama" --> True
# "Hello" --> False

def strng(st):
    s = ''
    for i in st:
        s = s + i.lower()
    s1 = s.replace(' ', '')
    if s1 == s1[::-1]:
        return True
    else:
        return False

print(strng('A man a plan a canal Panama'))