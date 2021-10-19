import numpy as np
from scipy.optimize import minimize
import math

#Oct 15 Riddler Express https://fivethirtyeight.com/features/can-you-hit-these-riddles-out-of-the-park/
def average_games(p = 0.5, a=0, b=0):
    if a == 4 or b == 4:
        return (a+b)
    else:
        return p*average_games(p, a+1, b)+ (1-p)*average_games(p, a, b+1)
#print(average_games())
    
#Oct 8 Riddler Express https://fivethirtyeight.com/features/can-you-evade-your-evil-twin/
def f(x):
    y = ((10000000)*(x/(x+10)))-x
    return -y

# x0 = np.array([1000]) #guess
# ans = minimize(f, x0, method = "Nelder-Mead", options = {'disp': True})
# print(str(ans.x))

#September 24 Riddler Classic https://fivethirtyeight.com/features/can-you-climb-your-way-to-victory/

#August 13 Riddler Express https://fivethirtyeight.com/features/are-you-clever-enough/
def clever():
    ans = 0
    for i in range(10):
        percent_cleverest = (math.comb(9,i)*((0.9)**(9-i)*(0.1**(i)))*(1/(1+i)))
        ans += percent_cleverest
    return ans

#print(clever())