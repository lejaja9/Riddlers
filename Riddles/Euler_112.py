#Project Euler Question 112 https://projecteuler.net/problem=112

def not_bouncy(n):
    if n < 10:
        return True
    increasing, decreasing = True, True
    number = n
    last_digit = n%10
    while number > 9 and (increasing or decreasing):
        number = number//10
        second_to_last_digit = number%10
        if increasing:
            if second_to_last_digit < last_digit:
                increasing = False
        if decreasing:
            if second_to_last_digit > last_digit:
                decreasing = False
        last_digit = second_to_last_digit
    return increasing or decreasing


bouncy = 269
nott_bouncy = 269
i = 539
while bouncy/ (bouncy+nott_bouncy) != 0.99:
    if not_bouncy(i):
        nott_bouncy += 1
    else:
        bouncy += 1
    i += 1

print(i-1)