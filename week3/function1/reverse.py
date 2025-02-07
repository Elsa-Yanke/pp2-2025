def reverse(s):
    w = s.split()  
    l = w[::-1]
    return ' '.join(l)


if __name__ == "__main__":
    r = input()
    print(reverse(r))
            