#January 28 Riddler Classic https://fivethirtyeight.com/features/can-you-tune-up-the-truck/

def oil_change(months):
    oil = {}
    #initialize old tank of oil
    for i in range(1, 13):
        oil[i] = 1
    #subsequent oil changes
    for i in range(13, months+13):
        for key in oil:
            oil[key] *= (11/12)
        oil[i] = 1
    #adding how many quarts of new oil is in the car
    new_quarts = 0
    for i in range(months+12, months, -1):
        new_quarts += oil[i]

    return new_quarts

print(oil_change(19))

ans = 1

for i in range(1, 12):
    ans += (11/12)**i

print(12 - ans)