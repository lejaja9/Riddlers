#March 18 Riddler Classic https://fivethirtyeight.com/features/is-it-anyones-birthday/

import math

def encode(n):
    global ans
    ans = []
    
    def fibo(a, b):
        global ans
        seq = [a, b]
        while seq[-2]-seq[-1] <= seq[-1] and seq[-2]-seq[-1] > 0:
            seq.append(seq[-2]-seq[-1])
        if len(seq) > len(ans):
            ans = seq
        #print(seq)
        return

    for i in range(math.ceil(n/2), n):
        fibo(i, n-i)
    
    return ans, (ans[-1], ans[-2], len(ans)-1)

print(encode(81))
print(encode(179))