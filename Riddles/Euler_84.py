#Project Euler #84 https://projecteuler.net/problem=84

import numpy as np
from itertools import chain

#transition matrix with no movement (every space has an equal 2.5% chance of landing)
matrix = np.zeros((40,40))
prob = {2:(1/16), 3:(2/16), 4:(4/16), 5:(4/16), 6:(3/16), 7:(2/16), 8:(1/16)}

for row in range(len(matrix)):
    for col in range(2, 9):
        matrix[row][(col+row)%40] = prob[col]

#print(np.sum(matrix, axis = 1))

#community chest at positions 2, 17, and 33
for row in range(len(matrix)):
    if matrix[row][2] != 0:
        temp = matrix[row][2]
        matrix[row][2] *= (7/8)
        matrix[row][0] += (1/16)*temp
        matrix[row][10] += (1/16)*temp

for row in range(len(matrix)):
    if matrix[row][17] != 0:
        temp = matrix[row][17]
        matrix[row][17] *= (7/8)
        matrix[row][0] += (1/16)*temp
        matrix[row][10] += (1/16)*temp

for row in range(len(matrix)):
    if matrix[row][33] != 0:
        temp = matrix[row][33]
        matrix[row][33] *= (7/8)
        matrix[row][0] += (1/16)*temp
        matrix[row][10] += (1/16)*temp

#print(np.sum(matrix, axis = 1))

#chance at positions 7, 22, 36
for row in range(len(matrix)):
    if matrix[row][7] != 0:
        temp = matrix[row][7]
        matrix[row][7] *= (6/16)
        matrix[row][0] += (1/16)*temp
        matrix[row][10] += (1/16)*temp
        matrix[row][11] += (1/16)*temp
        matrix[row][24] += (1/16)*temp
        matrix[row][39] += (1/16)*temp
        matrix[row][5] += (1/16)*temp
        #next railroad
        matrix[row][15] += (2/16)*temp
        #next utility
        matrix[row][12] += (1/16)*temp
        #3 spaces back
        matrix[row][4] += (1/16)*temp

for row in range(len(matrix)):
    if matrix[row][22] != 0:
        temp = matrix[row][22]
        matrix[row][22] *= (6/16)
        matrix[row][0] += (1/16)*temp
        matrix[row][10] += (1/16)*temp
        matrix[row][11] += (1/16)*temp
        matrix[row][24] += (1/16)*temp
        matrix[row][39] += (1/16)*temp
        matrix[row][5] += (1/16)*temp
        #next railroad
        matrix[row][25] += (2/16)*temp
        #next utility
        matrix[row][28] += (1/16)*temp
        #3 spaces back
        matrix[row][19] += (1/16)*temp

for row in range(len(matrix)):
    if matrix[row][36] != 0:
        temp = matrix[row][36]
        matrix[row][36] *= (6/16)
        matrix[row][0] += (1/16)*temp
        matrix[row][10] += (1/16)*temp
        matrix[row][11] += (1/16)*temp
        matrix[row][24] += (1/16)*temp
        matrix[row][39] += (1/16)*temp
        matrix[row][5] += (1/16)*temp
        #next railroad
        matrix[row][5] += (2/16)*temp
        #next utility
        matrix[row][12] += (1/16)*temp
        #3 spaces back (this time, Community Chest)
        matrix[row][33] += (1/16)*temp*(14/16)
        matrix[row][0] += (1/16)*temp*(1/16)
        matrix[row][10] += (1/16)*temp*(1/16)

#print(np.sum(matrix, axis = 1))

#Go to Jail square
for row in range(len(matrix)):
    if matrix[row][30] != 0:
        temp = matrix[row][30]
        matrix[row][10] += temp
        matrix[row][30] = 0

#print(np.sum(matrix, axis = 1))

#Rolling 3 doubles in a row
matrix = matrix*(215/216)
for row in range(len(matrix)):
    matrix[row][10] += (1/216)

#print(np.sum(matrix, axis = 1))


#initial distribution vector
initial = np.zeros((40, 1))
initial[0][0] = 1

matrix = np.transpose(matrix)

steady_state_matrix = np.linalg.matrix_power(matrix, 900)

answer = np.dot(steady_state_matrix, initial)

answer = list(chain.from_iterable(answer))

list = []
for i in range(len(answer)):
    list.append([i, answer[i]])

list.sort(key=lambda x: x[1], reverse = True)

print(list)