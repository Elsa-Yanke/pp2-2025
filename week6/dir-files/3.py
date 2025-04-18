import os

path = input()

if os.path.exists(path):
    dir = os.path.dirname(path)
    filename = os.path.basename(path)
    print("Filename:", filename)
    print("Directory:", dir)
