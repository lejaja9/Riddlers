#December 23 Riddler Express https://fivethirtyeight.com/features/can-you-outwit-the-tax-collector/

#    HAPPY 
# HOLIDAYS 
# HOHOHOHO

#A D H I L O P S Y
#0 1 2 3 4 5 6 7 8

#rules: L+1 = H, H+I >= 10, (Y+S)%10 = O

def permute(num_list):
    ans = []

    def helper(cume, mod_num_list):
        if len(cume) == 9:
            if (int(cume[4])+1 == int(cume[2])) and ((int(cume[4])+int(cume[2])) >= 10) and ((int(cume[7])+int(cume[8]))%10 == int(cume[5])):
                ans.append(cume.copy())
            return
        for i in range(len(mod_num_list)):
            cume.append(mod_num_list[i])
            helper(cume, mod_num_list[:i] + mod_num_list[i+1:])
            cume.pop()
    helper([], num_list)
    print(len(ans))
    return ans


def addition(numbers):
    happy = int(numbers[2] + numbers[0] + numbers[6] + numbers[6] + numbers[8])
    holidays = int(numbers[2] + numbers[5] + numbers[4] + numbers[3] + numbers[1] + numbers[0] + numbers[8] + numbers[7])
    hohohoho = int(numbers[2] + numbers[5] + numbers[2] + numbers[5] + numbers[2] + numbers[5] + numbers[2] + numbers[5])
    if happy+holidays == hohohoho:
        print(happy, holidays, hohohoho)
        return True
    return False

for p in permute(['0','1','2','3','4','5','6','7','8','9']):
    if addition(p) == True:
        print(p)

# 84661 80723419 80808080
# ['4', '3', '8', '2', '7', '0', '6', '9', '1']
# 68332 61547829 61616161
# ['8', '7', '6', '4', '5', '1', '3', '9', '2']
