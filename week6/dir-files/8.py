import os

path = input()

if os.path.exists(path) & os.access(path, os.F_OK):
    os.remove(path)
else:
    print("Path doesnt exist")