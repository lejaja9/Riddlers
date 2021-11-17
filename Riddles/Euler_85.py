#Project Euler Question 85 https://projecteuler.net/problem=85

def num_rec(m,n):
    num = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            rec = (m-i+1)*(n-j+1)
            num += rec
    return num


ans = [2000000,0,0]
m = 1
n = 1
gap = 2000000
while True:
    temp_gap = abs(2000000 - num_rec(m, n))
    if temp_gap < gap:
        gap = temp_gap
        n += 1
    else:
        if gap < ans[0]:
            ans = [gap, m, n-1]
        if m > n:
            print(ans)
            break
        m += 1
        n = 1
        gap = 2000000