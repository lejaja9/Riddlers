#Project Euler Question 90 https://projecteuler.net/problem=90

def combinations(n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], r = 6):
    ans = []

    def helper(cume, numbers_list):
        if len(cume) == r:
            if cume not in ans:
                ans.append(cume.copy())
            return
        for i in range(len(numbers_list)):
            cume.append(numbers_list[i])
            helper(cume, numbers_list[i+1:])
            cume.pop()

    helper([], n)
    return ans

#01, 04, 09, 16, 25, 36, 49, 64, 81
def check(dice_pair):
    dice1 = dice_pair[0]
    dice2 = dice_pair[1]

    #01
    if (0 in dice1 and 1 in dice2) or (1 in dice1 and 0 in dice2):
        #04
        if (0 in dice1 and 4 in dice2) or (4 in dice1 and 0 in dice2):
            #09
            if (0 in dice1 and (6 in dice2 or 9 in dice2)) or ((6 in dice1 or 9 in dice1) and 0 in dice2):
                #16
                if (1 in dice1 and (6 in dice2 or 9 in dice2)) or ((6 in dice1 or 9 in dice1) and 1 in dice2):
                    #25
                    if (2 in dice1 and 5 in dice2) or (5 in dice1 and 2 in dice2):
                        #36
                        if (3 in dice1 and (6 in dice2 or 9 in dice2)) or ((6 in dice1 or 9 in dice1) and 3 in dice2):
                            #49
                            if (4 in dice1 and (6 in dice2 or 9 in dice2)) or ((6 in dice1 or 9 in dice1) and 4 in dice2):
                                #64
                                if (4 in dice1 and (6 in dice2 or 9 in dice2)) or ((6 in dice1 or 9 in dice1) and 4 in dice2):
                                    #81
                                    if (8 in dice1 and 1 in dice2) or (1 in dice1 and 8 in dice2):
                                        return True
    return False

dice = combinations()

pairs = combinations(dice, 2)

ans = 0
for pair in pairs:
    if check(pair):
        ans += 1

print(ans)
