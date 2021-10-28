#Project Euler Question 32 https://projecteuler.net/problem=32

def one_nine(a,b,c):
    a1 = str(a)
    a2 = str(b)
    a3 = str(c)
    a4 = a1+a2+a3
    if len(a4) == 9 and set(a4) == set('123456789'):
        return True
    return False

ans = []
for i in range(1, 10):
    for j in range(1000, 10000):
        if one_nine(i, j, i*j):
            if i*j not in ans:
                ans.append((i, j, i*j))

for i in range(10, 100):
    for j in range(100, 1000):
        if one_nine(i, j, i*j):
            if i*j not in ans:
                ans.append((i, j, i*j))

print(ans)