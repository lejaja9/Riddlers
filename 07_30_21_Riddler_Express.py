#July 30 Riddler Express https://fivethirtyeight.com/features/will-riddler-nation-win-gold-in-archery/

def arrows():
    ans = []
    list = [10, 9, 5]
    global below24
    below24 = 0
    global at24
    at24 = 0
    global above24
    above24 = 0

    def permute(cume = []):
        global below24
        global at24
        global above24
        if len(cume) == 3:
            if cume not in ans:
                ans.append(cume.copy())
                #print(sum(cume))
            if sum(cume) < 24:
                below24 += 1
            elif sum(cume) == 24:
                at24 += 1
            else:
                above24 += 1
            return
        else:
            for i in range(len(list)):
                cume.append(list[i])
                permute(cume)
                cume.pop()
    permute()
    return above24, (below24+above24)

print(arrows())