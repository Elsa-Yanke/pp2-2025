import math

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)+ 1)):
        if a % i == 0:
            return False
    return True
        
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers: ").split()))
    print(filter_prime(numbers))