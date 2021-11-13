# 11-12-21 Riddler Express https://fivethirtyeight.com/features/can-you-stick-it-to-the-genie/

#d4, d6, d8 dice
denom = 4*6*8
nume = 0
for i in range(1,5):
    for j in range(i+1,7):
        for k in range(j+1,9):
            nume += 1
print(nume, denom)

#extra credit, d4, d6, d8, d10, d12 and d20
denom = 4*6*8*10*12*20
nume = 0
for i in range(1,5):
    for j in range(i+1,7):
        for k in range(j+1,9):
            for l in range(k+1, 11):
                for m in range(l+1, 13):
                    for n in range(m+1, 21):
                        nume += 1
print(nume, denom)