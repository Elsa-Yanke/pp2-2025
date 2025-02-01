def solve(numheads, numlegs):
    rab = int((numlegs - (numheads * 2)) / 2)
    chic = int(numheads - rab)
    print (f"chicken = {chic}", f"rabbits = {rab}")

numheads = int(input())
numlegs = int(input())
solve(numheads, numlegs)