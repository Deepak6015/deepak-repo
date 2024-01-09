#Q3

def is_prime():
    n = int(input("Enter a positive integer: "))
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print("%d is not a prime number." % n)
                break
        else:
            print("%d is a prime number." % n)
    else:
        print("%d is not a prime number." % n)

is_prime()