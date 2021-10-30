# 10/29/21 Riddler Classic https://fivethirtyeight.com/features/can-you-survive-squid-game-riddler/
from math import comb
import time
start_time = time.time()

ans = 18*(0.5**18)*15
ans += comb(18,2)*(0.5**18)*(14)
ans += comb(18,9)*(0.5**18)*7

for i in range(3,9):
    ans += comb(18,i)*(0.5**18)*(14)

print(ans)
print("--- %s seconds ---" % (time.time() - start_time))