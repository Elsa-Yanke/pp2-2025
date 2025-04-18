import math
import time

a = int(input())
b = int(input())

time.sleep(b/1000)
result = math.sqrt(a)

print(f"Square root of {a} after {b} milliseconds is {result}")