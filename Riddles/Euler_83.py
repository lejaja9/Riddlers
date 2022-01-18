#Project Euler Question 83 https://projecteuler.net/problem=83

import time

start_time = time.time()

square_83 = []

with open('Riddles/Euler_83.txt', 'r') as file:
    for line in file:
        square_83.append([int(x) for x in line.rstrip().split(',')])

#square_83 = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]



def dijkstra(matrix):
    #initialize searched and unsearched sets
    unsearched = {}
    searched = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            unsearched[(i, j)] = float('Inf')

    def bfs(matrix_coordinate):
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        for (row, col) in directions:
            if (matrix_coordinate[0]+row, matrix_coordinate[1]+col) in unsearched:
                #print(matrix_coordinate[0]+row, matrix_coordinate[1]+col)
                unsearched[(matrix_coordinate[0]+row, matrix_coordinate[1]+col)] = min(unsearched[(matrix_coordinate[0]+row, matrix_coordinate[1]+col)], unsearched[matrix_coordinate]+matrix[matrix_coordinate[0]+row][matrix_coordinate[1]+col])
    
    #start at matrix[0][0]
    unsearched[(0, 0)] = matrix[0][0]
    bfs((0, 0))
    searched[(0, 0)] = unsearched[(0, 0)]
    del unsearched[(0, 0)]

    while len(unsearched) > 0:
        target_key = None
        smallest_distance = float('Inf')
        for key in unsearched:
            if unsearched[key] < smallest_distance:
                smallest_distance = unsearched[key]
                target_key = key
        bfs(target_key)
        searched[target_key] = unsearched[target_key]
        del unsearched[target_key]

    return searched[(len(matrix)-1, len(matrix[0])-1)]


print(dijkstra(square_83))

print("--- %s seconds ---" % (time.time() - start_time))
