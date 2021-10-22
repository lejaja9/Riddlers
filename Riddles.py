import numpy as np

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