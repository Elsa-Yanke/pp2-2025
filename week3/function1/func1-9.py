import math
def volume_of_sphere(r):
    return (4/3 * math.pi) * (r**3)

r = float(input())
print(volume_of_sphere(r))