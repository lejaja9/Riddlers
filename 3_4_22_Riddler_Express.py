#March 4 Riddler Express https://fivethirtyeight.com/features/can-you-crawl-around-the-cone/

from math import comb

heads_prob = []
dice_prob = []
hearts_prob = []
ans = 0

for i in range(4):
    heads_prob.append(comb(3, i) * (0.5**i) * (0.5**(3-i)))

for i in range(4):
    dice_prob.append(comb(3, i) * ((1/3)**i) * ((2/3)**(3-i)))

for i in range(4):
    nume = comb(13, i) * comb(39, 3-i)
    denom = comb(52, 3)
    hearts_prob.append(nume/denom)

for i in range(4):
    temp = heads_prob[i]*dice_prob[i]*hearts_prob[i]
    ans += temp

print(ans)