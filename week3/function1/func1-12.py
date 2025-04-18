def histogram(l):
    for i in range(len(l)):
        print('*' * l[i])

    return l

h = list(map(int(input().split())))
r = histogram(h)
