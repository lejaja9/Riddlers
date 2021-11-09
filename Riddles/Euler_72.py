#Project Euler #72 https://projecteuler.net/problem=72
import time
import math
start_time = time.time()

# def prime_factors(n):
#     list = []
#     divisor = 2
#     while divisor <= n:
#         while n%divisor == 0:
#             n = n/divisor
#             if divisor not in list:
#                 list.append(divisor)
#         divisor += 1
#     return list

# def gcf(a, b):
#     factors_b = prime_factors(b)
#     for factor in factors_b:
#         if a%factor == 0:
#             return False
#     return True

# list = []

# for i in range(2, 20000):
#     for j in range(1, i):
#         if gcd(i, j) == 1:
#             list.append((j,i))

# print(len(list))

# def prime():
#     list_of_primes = [2,3,5]
#     i = 6
#     for i in range(6, 1000000):
#         for prime in list_of_primes:
#             if i%prime == 0:
#                 break
#         else:
#             list_of_primes.append(i)
#     return list_of_primes

# print(prime())

def prime_less_than(n):
    if n == 0 or n == 1:
        return []
    list = [True]*n
    list[0], list[1] = False, False
    for i in range(2, math.ceil(math.sqrt(n))):
        if list[i] == True:
            for j in range(i*i, n, i):
                list[j] = False
    return [i for i in range(n) if list[i] == True]


primes = prime_less_than(1000001)

def totient_function(i, list = primes):
    result = i
    n = i
    while n != 1:
        for prime in primes:
            if n%prime == 0:
                result *= 1-(1/prime)
                while n%prime == 0:
                    n = n/prime
    return result

totient = [0]*1000001
set_primes = set(primes)
for i in range(2, len(totient)):
    #print(i)
    if i in set_primes:
        totient[i] = i-1
    else:
        for prime in primes:
            if i%prime == 0 and math.gcd(prime, int(i/prime)) == 1:
                totient[i] = int(totient[prime]*totient[int(i/prime)])
                break
        else:
            totient[i] = int(totient_function(i))

print(sum(totient))


print("--- %s seconds ---" % (time.time() - start_time))