# 11-5-21 Riddler Classic https://fivethirtyeight.com/features/how-many-friends-are-on-the-riddler-social-network/


def is_prime(n):
    for num in list_of_primes:
        if n%num == 0:
            return num
    return -1

def sum_factor(n):
    sum = 1
    for key in dict[n]:
        sum *= ((key**(dict[n][key]+1)) - 1) / (key-1)
    return sum


dict = {}

dict[2] = {2:1}
dict[3] = {3:1}

list_of_primes = [2,3]

number = 4

stop = 0

while stop != 3:
    if is_prime(number) == -1:
        list_of_primes.append(number)
        dict[number] = {number:1}
    else:
        divisor = int(number/is_prime(number))
        dict[number] = dict[divisor].copy()
        key = int(number/divisor)
        if key in dict[number]:
            dict[number][key] += 1
        else:
            dict[number][key] = 1

    if sum_factor(number) == int(round(number*2.54)):
        print(number)
        stop += 1
    number += 1

#print(sum([1, 2, 4, 5, 8, 10, 16, 20, 25, 31, 32, 40, 50, 62, 64, 80, 100, 124, 155, 160, 200, 248, 310, 320, 400, 496, 620, 775, 800, 992, 1240, 1550, 1600, 1984, 2480, 3100, 4960, 6200, 9920, 12400, 24800, 49600]))