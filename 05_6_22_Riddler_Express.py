#May 6 Riddler Express https://fivethirtyeight.com/features/can-you-build-the-longest-ladder/

import random

def elevator(height):
    pos = height
    stops = 0
    while pos != 1:
        pos = random.randint(1, pos-1)
        stops += 1
    
    return stops

def sims(num):
    cume = 0
    for i in range(num):
        cume += elevator(10)
    return cume/num

print(sims(1000000))