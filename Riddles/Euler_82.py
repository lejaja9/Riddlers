#Project Euler Question 82 https://projecteuler.net/problem=82

square_82 = []

with open('Riddles/Euler_82.txt', 'r') as file:
    for line in file:
        square_82.append([int(x) for x in line.rstrip().split(',')])


def min_path(matrix):
    #transpose for convenience
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    for i in range(1, len(matrix)):
        temp = [x + y for x, y in zip(matrix[i-1], matrix[i])]
        for j in range(1, len(temp)):
            temp[j] = min(temp[j], matrix[i][j]+temp[j-1])
        for k in range(len(temp)-2, -1, -1):
            temp[k] = min(temp[k], matrix[i][k]+temp[k+1])
        matrix[i] = temp
    return min(matrix[-1])

print(min_path(square_82))