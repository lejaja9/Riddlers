#Project Euler #64 https://projecteuler.net/problem=64
import math

def period(x):
    #perfect square
    if math.sqrt(x)%1 == 0:
        return 0
    #converging fractions
    representation = []
    remainder_set = set()

    quotient = math.floor(math.sqrt(x))
    remainder = math.sqrt(x) - quotient

    representation.append(quotient)
    remainder_set.add(round(remainder,9))
    while True:
        x = 1/remainder
        quotient = math.floor(x)
        remainder = x - quotient
        if round(remainder,9) in remainder_set:
            break
        else:
            representation.append(quotient)
            remainder_set.add(round(remainder,9))
    
    return len(representation)


ans = 0
for i in range(1000):
    if period(i)%2 == 1:
        ans += 1
        print(i)

print(ans)
