#April 8 Riddler Express https://fivethirtyeight.com/features/can-you-be-mediocre-enough-to-win/

class three_x_three:

    def __init__(self):
        self.board = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]
        self.coordinates = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
        self.combinations = []

    def print(self):
        for row in self.board:
            print(row)

    def generate_combinations(self):
        for i in range(1, 8):
            for j in range(i+1, 9):
                for k in range(j+1, 10):
                    self.combinations.append((i, j, k))

    def three_in_a_row(self, points):
        #non-diagonal
        if (points[0][0] == points[1][0] == points[2][0]) or (points[0][1] == points[1][1] == points[2][1]):
            return True
        #diagonal
        if (set(points) == set([(0, 0), (1, 1), (2, 2)])) or (set(points) == set([(2, 0), (1, 1), (0, 2)])):
            return True
        else:
            return False

    def get_values(self):
        for c in self.combinations:
            if self.three_in_a_row([self.coordinates[c[0]], self.coordinates[c[1]], self.coordinates[c[2]]]):
                self.board[self.coordinates[c[0]][0]][self.coordinates[c[0]][1]] += 1
                self.board[self.coordinates[c[1]][0]][self.coordinates[c[1]][1]] += 1
                self.board[self.coordinates[c[2]][0]][self.coordinates[c[2]][1]] += 1

    
# test = three_x_three()
# test.generate_combinations()
# test.get_values()
# test.print()



class three_x_three_x_three:

    def __init__(self):
        self.board = [[[0]*3 for i in range(3)] for i in range(3)]
        self.combinations = None

    def print_board(self):
        for row in self.board:
            print(row)

    def points(self, numbers):
        ans = []
        permutations = []

        def permute(cume, list):
            if len(cume) == 3:
                if cume not in ans:
                    permutations.append(cume.copy())
                    return
            for i in range(len(list)):
                cume.append(list[i])
                permute(cume, list)
                cume.pop()

        permute([], numbers)

        def combine(cume2, list2):
            if len(cume2) == 3:
                ans.append(cume2.copy())
                return
            for i in range(len(list2)):
                cume2.append(list2[i])
                combine(cume2, list2[i+1:])
                cume2.pop()
        
        combine([], permutations)

        self.combinations = ans

    def three_in_a_row(self, points):
        #same horizontal plane
        if (points[0][0] == points[1][0] == points[2][0]):
            #straight
            if (points[0][1] == points[1][1] == points[2][1]) or (points[0][2] == points[1][2] == points[2][2]):
                return True
            #diagonal
            elif (set([(points[0][1], points[0][2]), (points[1][1], points[1][2]), (points[2][1], points[2][2])]) == set([(0, 0), (1, 1), (2, 2)])) or (set([(points[0][1], points[0][2]), (points[1][1], points[1][2]), (points[2][1], points[2][2])]) == set([(2, 0), (1, 1), (0, 2)])):
                return True
            else:
                return False
        #same vertical plane
        elif (points[0][1] == points[1][1] == points[2][1]):
            #straight vertical, because horizontal already accounted for
            if (points[0][2] == points[1][2] == points[2][2]):
                return True
            #diagonal
            elif (set([(points[0][0], points[0][2]), (points[1][0], points[1][2]), (points[2][0], points[2][2])]) == set([(0, 0), (1, 1), (2, 2)])) or (set([(points[0][0], points[0][2]), (points[1][0], points[1][2]), (points[2][0], points[2][2])]) == set([(2, 0), (1, 1), (0, 2)])):
                return True
            else:
                return False
        #side diagonal:
        elif (points[0][2] == points[1][2] == points[2][2]):
            #only need to account for diagonal
            if (set([(points[0][0], points[0][1]), (points[1][0], points[1][1]), (points[2][0], points[2][1])]) == set([(0, 0), (1, 1), (2, 2)])) or (set([(points[0][0], points[0][1]), (points[1][0], points[1][1]), (points[2][0], points[2][1])]) == set([(2, 0), (1, 1), (0, 2)])):
                return True
            else:
                return False
        #3D diagonal, hard code the 4 cases
        elif set([(points[0][0], points[0][1], points[0][2]), (points[1][0], points[1][1], points[1][2]), (points[2][0], points[2][1], points[2][2])]) == set([(0, 0, 0), (1, 1, 1), (2, 2, 2)]) or \
            set([(points[0][0], points[0][1], points[0][2]), (points[1][0], points[1][1], points[1][2]), (points[2][0], points[2][1], points[2][2])]) == set([(0, 0, 2), (1, 1, 1), (2, 2, 0)]) or \
                set([(points[0][0], points[0][1], points[0][2]), (points[1][0], points[1][1], points[1][2]), (points[2][0], points[2][1], points[2][2])]) == set([(0, 2, 0), (1, 1, 1), (2, 0, 2)]) or \
                    set([(points[0][0], points[0][1], points[0][2]), (points[1][0], points[1][1], points[1][2]), (points[2][0], points[2][1], points[2][2])]) == set([(0, 2, 2), (1, 1, 1), (2, 0, 0)]):
            return True
        else:
            return False

    def get_values(self):
        for c in self.combinations:
            if self.three_in_a_row(c):
                self.board[c[0][0]][c[0][1]][c[0][2]] += 1
                self.board[c[1][0]][c[1][1]][c[1][2]] += 1
                self.board[c[2][0]][c[2][1]][c[2][2]] += 1


test = three_x_three_x_three()
test.points([0, 1, 2])
test.get_values()
test.print_board()