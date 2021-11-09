#Project Euler Question #3 https://projecteuler.net/problem=3

n = 600851475143

prime_factors = []

divisor = 2

while divisor <= n:
    while n%divisor == 0:
        n = n/divisor
        if divisor not in prime_factors:
            prime_factors.append(divisor)
    divisor += 1

print(prime_factors)