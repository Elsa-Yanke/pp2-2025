import convertgrams
import reverse
import isprime

print("Which function would you like to use?")
print("Pick 1 if you want to convert into ounces.")
print("Pick 2 if you want to reverse string.")
print("Pick 3 if you want to filter the list by leaving prime numbers.")

ch = int(input())


if ch == 1:
    n = int(input("Enter your number:"))
    convertgrams.convertounces(n)
elif ch == 2:
    s = input("Enter your sentences:")
    reverse.reverse(s)
elif ch ==3 :
    numbers = list(map(int, input("Enter numbers of your list: ").split()))
    print(isprime.filter_prime(numbers))
