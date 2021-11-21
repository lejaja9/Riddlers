#November 19, 2021 Riddler Express Simulation https://fivethirtyeight.com/features/are-you-the-fittest-gym-rat/

import numpy as np

nume = 0
denom = 0

for i in range(1000000):
    rand1 = np.random.uniform(0,1)
    rand2 = np.random.uniform(0,1)
    if rand2 < rand1: #at gym
        denom += 1
        if rand1 > 0.5: #at gym more often than you
            nume += 1
    
print(nume/denom)
