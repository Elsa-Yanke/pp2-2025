def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    return s == s[::-1]

text = input()
if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")              