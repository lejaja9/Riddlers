#August 13 Riddler Express https://fivethirtyeight.com/features/are-you-clever-enough/
import math

def clever():
    ans = 0
    for i in range(10):
        percent_cleverest = (math.comb(9,i)*((0.9)**(9-i)*(0.1**(i)))*(1/(1+i)))
        #print(i, percent_cleverest)
        ans += percent_cleverest
    return ans

print(clever())