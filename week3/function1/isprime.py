import math

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)+ 1)):
        if a % i == 0:
            return False
    return True
        
def filter_prime(num):
    prime_num = []
    for x in num:
        if is_prime(x):
            prime_num.append(x)
    return prime_num

if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers: ").split()))
    print(filter_prime(numbers))