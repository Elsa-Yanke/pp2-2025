import os

path = input()

if os.path.exists(path):
    if os.access(path, os.F_OK):
        print("Path exist")
    if os.access(path, os.R_OK):
        print("Path is readable")
    if os.access(path, os.W_OK):
        print("Path is writable")
    if os.access(path, os.X_OK):
        print("Path is executable")
else:
    print("Path doesnt exist")
