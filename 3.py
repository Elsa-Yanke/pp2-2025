def fib(n):
    a1 = 0
    a2 = 1
    for i in range(n):
        if i == 1 or i == 0:
            yield i
        else:
            num = a1 + a2
            a1 = a2
            a2 = num
            yield num

for i in fib(8):
    print(i)