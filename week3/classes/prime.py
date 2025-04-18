import math
def filter_prime(p_numbs):
    is_prime = filter(lambda x: x > 1 and all(x%i != 0 for i in range(2, int(math.sqrt(x))+ 1)),p_numbs)
    return list(is_prime)

p_numbs = list(map(int,(input().split())))
print(filter_prime(p_numbs))