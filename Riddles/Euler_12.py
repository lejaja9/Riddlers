#Project Euler Question 12 https://projecteuler.net/problem=12

def num_of_divisors(x):
    if x == 1:
        return 1

    number = 1

    def prime_factorization(n):
        if n == 1:
            return 1
        
        dividend = n
        divisor = 2
        factorization = {}

        while dividend != 1:
            while dividend%divisor == 0:
                dividend = dividend/divisor
                if divisor in factorization:
                    factorization[divisor] += 1
                else:
                    factorization[divisor] = 1
            divisor += 1
        return factorization

    dict = prime_factorization(x)
    for key in dict:
        number = number*(dict[key]+1)

    return number


triangle_number = 1
addition = 2

while num_of_divisors(triangle_number) < 500:
    triangle_number = triangle_number + addition
    addition += 1

print(triangle_number)