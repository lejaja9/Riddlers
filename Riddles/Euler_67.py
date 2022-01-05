#Project Euler 67 https://projecteuler.net/problem=67

triangle = []
with open('Riddles/Euler_67.txt', 'r') as file:
    for line in file:
        triangle.append([int(x) for x in line.rstrip().split(' ')])


def max_total(triangle_list):
    for i in range(len(triangle_list)-2, -1, -1):
        for j in range(len(triangle_list[i])):
            triangle_list[i][j] += max(triangle_list[i+1][j], triangle_list[i+1][j+1])
    return triangle_list[0][0]

print(max_total(triangle))