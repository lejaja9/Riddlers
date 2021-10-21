from sklearn.utils import shuffle
import numpy as np
from scipy.optimize import minimize
import scipy.integrate as integrate
import math

#Oct 20 Teaser on run with friend: "Calculate pi with random number generator" (9 is my favorite number)
def darts():
    nume = 0
    for i in range(999999):
        x = np.random.uniform(0, 18)
        y = np.random.uniform(0, 18)
        distance = np.sqrt((x-9)**2 + (y-9)**2)
        if distance < 9:
            nume += 1
    return 4*nume/999999

print(darts())



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
def places():
    mini = 512
    maxi = 0
    list1 = shuffle(list(range(1,9)))
    list2 = shuffle(list(range(1,9)))
    list3 = shuffle(list(range(1,9)))
    #print(list1, list2, list3)
    for i in range(8):
        score = list1[i]*list2[i]*list3[i]
        #print(score)
        mini = min(mini, score)
        maxi = max(maxi, score)
    return mini, maxi

# win_scores = []
# lose_scores = []
# for i in range(9):
#      minny, verstappen = places()
#      win_scores.append(minny)
#      lose_scores.append(verstappen)
# print(max(win_scores), min(lose_scores))



#August 13 Riddler Express https://fivethirtyeight.com/features/are-you-clever-enough/
def clever():
    ans = 0
    for i in range(10):
        percent_cleverest = (math.comb(9,i)*((0.9)**(9-i)*(0.1**(i)))*(1/(1+i)))
        ans += percent_cleverest
    return ans

#print(clever())


#July 16 Riddler Express and Riddler Classic https://fivethirtyeight.com/features/can-you-win-the-penalty-shootout/
def f(x):
    return (x**2)+(1-x)**2

ans = integrate.quad(f, 0, 1)
#print(ans)

def penalty_simulation(p=0.7):
    team_a = 0
    team_b = 0
    count = 0

    # conditions
    # 6: count = 6, 3-0 or 0-3
    # 7: 4-1 (first team misses, second team makes)
    # 8: 4-1 (with miss) 

