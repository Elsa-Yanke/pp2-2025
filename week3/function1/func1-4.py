import math

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)+ 1)):
        if a % i == 0:
            return False
    return True
        
def filter_prime(num):
    return [num for num in numbers if is_prime(num)]

numbers = list(map(int, input().split()))
print(filter_prime(numbers))