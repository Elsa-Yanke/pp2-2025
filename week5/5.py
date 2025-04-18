import re

f = open("row.txt", 'r', encoding = "utf-8")
txt = f.read()
f.close()
find = r"\bа\w*б\b"
matches = re.search(find, txt)
if matches:
  print(matches.group())
else:
  print("no such string")