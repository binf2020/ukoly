import math

def PrimeGenerator():
    lower = 2
    upper = int(math.sqrt(n))
    primes = []
    for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

def PrimeFactors(n):
    while n % 2 == 0:
        print(2)
        n = n/2
    for i in range (3, int(math.sqrt(n))+1, 2) :
        while n % i == 0:
            print(i)
            n = n/i
    if n > 2:
        print(n)

x = int(input())
PrimeFactors(x)






""" for prime in primes:
    while True:
        #overit, zda je prime v num
        if n % prime == 0:
            print(prime)
            n = n / prime
        else:
            break """
            
