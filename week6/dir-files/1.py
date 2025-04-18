import os

path = input('enter your path: ')
all_items = os.listdir(path)

direct = []
file = []


for item in all_items:
    full_path = os.path.join(path,item)
    if os.path.isdir(full_path):
        direct.append(full_path)
    elif os.path.isfile(full_path):
        file.append(full_path)

print(f"ur directories is {direct}")
print(f"ur files is {file}")