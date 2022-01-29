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


print(next_gen([(-1, 0), (0, 0), (0, -1), (0, 1), (1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1)]))