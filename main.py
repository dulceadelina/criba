# Programa que implementa la criba de Erastótenes
# donde define los números primos de 2 hasta n
# Dulce Adelina Zuñiga Ramos
# 20/09/2020 - 21/09/2020

from math import isqrt


# here implements sieve of Eratosthenes and receives n
def sieve():                    # criba in english
    n = data()                  # ask for n
    while n < 2:               # beeing n a positive number
        n = data()

    criba = []                  # 1st step
    for i in range(0, n-1):     # build a n-length array
        criba.append(i+2)       # 2nd step: fill from 2 till n

    primes = []         # step three: take the first prime number

    for i in range(2, isqrt(n)):        # iterates from 2 until square root of n
        if criba[i-2] != 0:             # if the number isn't marked
            primes.append(criba[i-2])   # it takes as prime
            for j in range(0, n-1):     # iterate criba list
                if criba[j] % i == 0:   # if it's multiple of a prime number
                    criba[j] = 0        # mark with zero

    for c in criba:     # the rest are primes
        if c != 0:
            primes.append(c)

    for i in range(0, len(primes)):
        if i % 10 == 0:
            print('')
        print(primes[i], end='\t')


# function that asks for the input, in this case: n
def data():
    n = int(input("Ingrese n: "))
    return n


if __name__ == '__main__':
    sieve()
    print('')
