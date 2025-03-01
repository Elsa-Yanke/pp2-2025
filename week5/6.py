import re
f = open("row.txt", 'r', encoding = "utf-8")
txt = f.read()
f.close()
find = re.sub(r'[ ,.]', ":",txt)
print(find)