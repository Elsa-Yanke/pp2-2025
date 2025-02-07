def convertounces(grams):
    ounces = 28.3495231 * grams
    print(ounces)

if __name__ == "__main__":
    grams = int(input())
    print(convertounces(grams))
