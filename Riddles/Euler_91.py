#Project Euler Question 91 https://projecteuler.net/problem=91

def combine(list, n):
    ans = []

    def helper(cume, n, k):
        if len(cume) == n:
            ans.append(cume.copy())
            return
        for i in range(k, len(list)):
            cume.append(list[i])
            helper(cume, n, i+1)
            cume.pop()

    helper([], n, 0)
    return ans

def parallel(pair1, pair2):
    rise1 = pair1[0][1]-pair1[1][1]
    run1 = pair1[0][0]-pair1[1][0]
    try:
        slope1 = (rise1/run1)
    except:
        slope1 = float("Inf")
    rise2 = pair2[0][1]-pair2[1][1]
    run2 = pair2[0][0]-pair2[1][0]
    try:
        slope2 = (rise2/run2)
    except:
        slope2 = float("Inf")

    if slope1 == float("Inf") or slope2 == float("Inf") or slope1 == 0 or slope2 == 0:
        if (slope1 == float("Inf") and slope2 == 0) or (slope2 == float("Inf") and slope1 == 0):
            return True
        else:
            return False
    elif ((-1/slope2)-0.0001 <= slope1 <= (-1/slope2)+0.0001): #rounding error
        return True
    else:
        return False


list = []
for i in range(0, 51):
    for j in range(0, 51):
        if (i,j) != (0,0):
            list.append((i,j))

pairs = combine(list,2)
#print(len(pairs))

ans = 0
for pair in pairs:
    if parallel([(0,0), pair[0]], [(0,0), pair[1]]) or parallel([(0,0), pair[0]], pair) or parallel([(0,0), pair[1]], pair):
        ans += 1

print(ans)
