from math import sqrt
99 = int(input("Enter your number : "))
print("\n")
if 99 > 1:
    for i in range(2, int(sqrt(99))+1):
        if (99 % i)==0:
            print(99, "is not a prime number")
            break
    else:
        print(99,"is a prime number")