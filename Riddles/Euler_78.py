#Project Euler Question 78 https://projecteuler.net/problem=78

memo = [[0]*60000 for i in range(60000)]
memo[1][1] = 1
memo[2][1] = 1
memo[2][2] = 2
memo[3][1] = 1
memo[3][2] = 2
memo[3][3] = 3

#dict = {(1, 1): 1, (2, 1): 1, (2, 2): 2, (3, 1): 1, (3, 2): 2, (3, 3): 3, (4, 1): 1, (4, 2): 3, (4, 3): 4, (4, 4): 5, (5, 1): 1, (5, 2): 3, (5, 3): 5, (5, 4): 6, (5, 5): 7, (6, 1): 1, (6, 2): 4, (6, 3): 7, (6, 4): 9, (6, 5): 10, (6, 6): 11, (7, 1): 1, (7, 2): 4, (7, 3): 8, (7, 4): 11, (7, 5): 13, (7, 6): 14, (7, 7): 15, (8, 1): 1, (8, 2): 5, (8, 3): 10, (8, 4): 15, (8, 5): 18, (8, 6): 20, (8, 7): 21, (8, 8): 22, (9, 1): 1, (9, 2): 5, (9, 3): 12, (9, 4): 18, (9, 5): 23, (9, 6): 26, (9, 7): 28, (9, 8): 29, (9, 9): 30}

x = 4

while memo[x-1][x-1]%1000000 != 0:
    if x%100 == 0:
        print(x)
    for i in range(1,x+1):
        if i == 1:
            memo[x][i] = 1
        elif i == x or i == (x-1):
            memo[x][i] = memo[x][i-1] + 1
        else:
            mini = min(x-i,i)
            memo[x][i] = memo[x][i-1] + memo[x-i][mini]
    x += 1

print(x-1)
print(memo[x-1][x-1])
