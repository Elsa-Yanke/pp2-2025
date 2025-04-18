def reverse(s):
    w = s.split()  
    w.reverse()
    print(" ".join(w))


if __name__ == "__main__":
    r = input()
    reverse(r)
            