#Project Euler Question 19 https://projecteuler.net/problem=19

dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 0:31}

day = 1 #Jan 1, 1900
year = 1900
month = 1
ans = 0

while year < 2001:
    month = month%12
    if day%7 == 0 and year > 1900:
        ans += 1
    day += dict[month] #move forward month
    if month == 2 and year%4 == 0 and year%100 != 0:  #leap year
        day += 1
    if month == 0:
        year += 1
    month += 1

print(ans)