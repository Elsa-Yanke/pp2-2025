import random
def hunran():
    yield random.randint(1, 100)

for i in hunran():
    print(i)