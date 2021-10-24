#July 23 Riddler Express https://fivethirtyeight.com/features/can-you-hop-across-the-chessboard/

def chess():
    ans = []
    dict = {'K': 'King', 'b':'Bishop', 'r':'Rook', 'n':'Knight', 'p':'Pawn', 'q':'Queen', 'BL':'black'}
    global searched
    searched = set()
    searched.add((6,4))
    global matrix
    matrix = [
    ['K', 'BL', 'b', 'BL', 'K', 'r', 'b', 'r'],
     ['n', 'r', 'n', 'n', 'p', 'n', 'K', 'b'],
     ['r', 'BL', 'n', 'BL', 'p', 'r', 'p', 'r'],
     ['BL', 'BL', 'p', 'r', 'BL', 'n', 'BL', 'BL'],
     ['n', 'n', 'n', 'b', 'BL', 'b', 'r', 'b'],
     ['q', 'r', 'n', 'p', 'BL', 'n', 'r', 'q'],
     ['BL', 'BL', 'r', 'p', 'b', 'p', 'b', 'q'],
     ['K', 'b', 'q', 'n', 'p', 'r', 'n', 'n']]
     #initial position is matrix[6][4], bishop
    b_moves = [[1,1], [1,-1], [-1,-1], [-1,1]]
    r_moves = [[1,0], [-1,0], [0,1], [0,-1]]
    n_moves = [[-1,2], [-2,1], [-2,-1], [-1,-2], [1,-2], [-2,1], [2,1], [1,2]]
    p_moves = [[-1,-1], [-1,1]]
    q_moves = b_moves+r_moves

    def search(row=6, col=4, pce='b', cume = [(6,4,'Bishop')]):
        global matrix
        global searched
        if pce == 'K':
            ans.append(cume.copy())
            return
        elif pce == 'BL':
            return
        #bishop
        elif pce == 'b':
            for rx, cx in b_moves:
                new_row = row + rx
                new_col = col + cx
                if 0 <= new_row <= 7 and 0 <= new_col <= 7 and (new_row, new_col) not in searched:
                    piece = matrix[new_row][new_col]
                    cume.append((new_row, new_col, dict[matrix[new_row][new_col]]))
                    searched.add((new_row, new_col))
                    search(new_row, new_col, piece, cume)
                    cume.pop()
        #rook
        elif pce == 'r':
            for rx, cx in r_moves:
                new_row = row + rx
                new_col = col + cx
                if 0 <= new_row <= 7 and 0 <= new_col <= 7 and (new_row, new_col) not in searched:
                    piece = matrix[new_row][new_col]
                    cume.append((new_row, new_col, dict[matrix[new_row][new_col]]))
                    searched.add((new_row, new_col))
                    search(new_row, new_col, piece, cume)
                    cume.pop()
        #knight
        elif pce == 'n':
            for rx, cx in n_moves:
                new_row = row + rx
                new_col = col + cx
                if 0 <= new_row <= 7 and 0 <= new_col <= 7 and (new_row, new_col) not in searched:
                    piece = matrix[new_row][new_col]
                    cume.append((new_row, new_col, dict[matrix[new_row][new_col]]))
                    searched.add((new_row, new_col))
                    search(new_row, new_col, piece, cume)
                    cume.pop()
        #pawn
        elif pce == 'p':
            for rx, cx in p_moves:
                new_row = row + rx
                new_col = col + cx
                if 0 <= new_row <= 7 and 0 <= new_col <= 7 and (new_row, new_col) not in searched:
                    piece = matrix[new_row][new_col]
                    cume.append((new_row, new_col, dict[matrix[new_row][new_col]]))
                    searched.add((new_row, new_col))
                    search(new_row, new_col, piece, cume)
                    cume.pop()
        #queen
        else:
            for rx, cx in q_moves:
                new_row = row + rx
                new_col = col + cx
                if 0 <= new_row <= 7 and 0 <= new_col <= 7 and (new_row, new_col) not in searched:
                    piece = matrix[new_row][new_col]
                    cume.append((new_row, new_col, dict[matrix[new_row][new_col]]))
                    searched.add((new_row, new_col))
                    search(new_row, new_col, piece, cume)
                    cume.pop()
    search()
    for path in ans:
        print(path)

print(chess())