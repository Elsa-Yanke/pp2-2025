def palindrome(str):
    str = str.replace(" ", "").lower()
    return str == str[::-1]
str = input()
if palindrome(str):
    print(True)
else:
    print(False)