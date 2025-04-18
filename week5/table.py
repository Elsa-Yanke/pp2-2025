import re
import csv
f = open("row.txt", 'r', encoding = "utf-8")
text = f.read()

BINpattern = r"\nБИН\s(?P<BIN>\d+)"
BINmatches = re.search(BINpattern, text).group("BIN")

print(BINmatches)

CHECKpattern = r"\nЧек\s(?P<CHECK>№\d+)"
CHECKmatches = re.search(CHECKpattern, text).group("CHECK") 

print(CHECKmatches)  

ItemPattern = r"(?P<RowNum>.*)\n(?P<ItemName>.*)\n(?P<ItemCount>.*)\sx\s(?P<ItemPrice>.*)\n(?P<TotalItemPrice>.*)\nСтоимость\n(?P<TotalItemPrice2>.*)"
ItemMatches = re.search(ItemPattern, text).group("ItemPrice") 
print(ItemMatches)

prog = re.compile(ItemPattern)
ItemIterator = prog.finditer(text)

with open ('table.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['RowNum', 'ItemName', 'ItemCount','ItemPrice','TotalItemPrice'])
    for ItemMatches in ItemIterator:
        writer.writerow([ItemMatches.group("RowNum"),ItemMatches.group("ItemName"), ItemMatches.group("ItemCount")])
        
        