#December 3 Riddler Express https://fivethirtyeight.com/features/can-you-slice-the-ice/

candles = [1,2,3,4]

def num_of_sums(list):
    #matrix
    matrix = [[0]*(sum(list)+1) for i in range(len(list)+1)]
    
    #base case
    for i in range(len(matrix)):
        matrix[i][0] = 1

    #dp
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if col < list[row-1]:
                matrix[row][col] = matrix[row-1][col]
            else:
                matrix[row][col] = matrix[row-1][col] + matrix[row-1][col-list[row-1]]

    return matrix[-1][1:]

print(num_of_sums(candles))