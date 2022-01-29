#January 28 Riddler Express https://fivethirtyeight.com/features/can-you-tune-up-the-truck/

original_points = [(-1, 0), (0, 0), (0, -1), (0, 1), (1, 0)]
#test = [(0,0), (0,-1), (0,1)]

def next_gen(list_of_points):
    searched_neighbors = set()
    shaded_points = set(list_of_points)
    new_generation = list_of_points.copy()

    def bfs(point):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for (x, y) in directions:
            neighboring_point = (point[0]+x, point[1]+y)
            if (neighboring_point in searched_neighbors) or (neighboring_point in shaded_points):
                continue
            else:
                searched_neighbors.add(neighboring_point)
                shaded_neighbors = 0
                for (x1, y1) in directions:
                    pointt = (neighboring_point[0]+x1, neighboring_point[1]+y1)
                    if pointt in shaded_points:
                        shaded_neighbors += 1
                if shaded_neighbors >= 3:
                    new_generation.append(neighboring_point)

    for p in list_of_points:
        bfs(p)
    
    return new_generation


g1 = original_points
print(g1, len(g1))
g2 = next_gen(g1)
print(g2, len(g2))
g3 = next_gen(g2)
print(g3, len(g3))
g4 = next_gen(g3)
print(g4, len(g4))
g5 = next_gen(g4)
print(g5, len(g5))
g6 = next_gen(g5)
print(g6, len(g6))
g7 = next_gen(g6)
print(g7, len(g7))
g8 = next_gen(g7)
print(g8, len(g8))
g9 = next_gen(g8)
print(g9, len(g9))
g10 = next_gen(g9)
print(g10, len(g10))