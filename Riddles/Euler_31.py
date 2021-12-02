#Project Euler 31 https://projecteuler.net/problem=31

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def coin_sums(listt, limit):
    ans = []

    def combinations(cume, i, sum):
        if sum == limit:
            ans.append(cume.copy())
            return
        elif i >= len(coins) or sum > limit:
            return

        cume.append(listt[i])
        combinations(cume, i, sum + listt[i])
        cume.pop(0)
        combinations(cume, i+1, sum)

    combinations([], 0, 0)
    return len(ans)

#print(coin_sums(coins, 200))

#dynamic programming solution

def coin_sums_dp(listt, limit):
    dp = [[0]*(limit+1) for i in range(len(listt)+1)]
    for row in range(1, len(dp)):
        for col in range(len(dp[0])):
            if row == 1 or col == 1:
                dp[row][col] = 1
            elif col < listt[row-1]:
                dp[row][col] = dp[row-1][col]
            else:
                dp[row][col] = dp[row-1][col] + dp[row][col-(listt[row-1])]
    return dp[-1][-1]


print(coin_sums_dp(coins, 200))

