def reverse(s):
    w = s.split()  
    l = w[::-1]
    return ' '.join(l)


r = input()
r1 = reverse(r)
print(r1)
            