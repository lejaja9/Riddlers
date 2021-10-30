# 10/29/21 Riddler Classic https://fivethirtyeight.com/features/can-you-survive-squid-game-riddler/
from math import comb
import time

start_time = time.time()

ans = 0
for i in range(1,16):
    ans += comb(18,i)*(0.5**18)*(16-i)

print(ans)
print("--- %s seconds ---" % (time.time() - start_time))

