#Oct 15 Riddler Express https://fivethirtyeight.com/features/can-you-hit-these-riddles-out-of-the-park/
def average_games(p = 0.5, a=0, b=0):
    if a == 4 or b == 4:
        return (a+b)
    else:
        return p*average_games(p, a+1, b)+ (1-p)*average_games(p, a, b+1)
print(average_games())