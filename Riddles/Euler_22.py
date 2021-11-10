#Project Euler #22 https://projecteuler.net/problem=22

names = open('Riddles/p022_names.txt', 'r')
names = names.read().split(',')
names.sort()


points = 0

for i in range(len(names)):
    score = 0
    for letter in names[i]:
        score += ord(letter)-64
    score += 60
    score = score*(i+1)
    points += score

print(points)

