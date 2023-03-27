def is_obstacle(start, end, direction, obstacles):
    for obstacle in obstacles:
        if direction == 'W' or direction == 'E':
            if obstacle[0] != start[0]:
                continue
            
            if direction == 'E':
                if start[1] <= obstacle[1] <= end[1]:
                    return True
            if end[1] <= obstacle[1] <= start[1]:
                return True
            
        elif direction == 'N' or direction == 'S':
            if obstacle[1] != start[1]:
                continue
            
            if direction == 'S':
                if start[0] <= obstacle[0] <= end[0]:
                    return True
            if end[0] <= obstacle[0] <= start[0]:
                return True
    return False
        

    
def solution(park, routes):
    H = len(park)
    W = len(park[0])
    point = None
    obstacles = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                point = [i, j]
                continue
            if park[i][j] == "X":
                obstacles.append([i,j])
    
    print(point)
    print(obstacles)
    
    for route in routes:
        direction = route.split(" ")[0]
        num = int(route.split(" ")[1])

        if direction == 'S':
            new_point = [point[0] + num, point[1]]

        elif direction == 'N':
            new_point = [point[0] - num, point[1]]

        elif direction == 'W':
            new_point = [point[0], point[1] - num]

        elif direction == 'E':
            new_point = [point[0], point[1] + num]
        
        if new_point[0] < 0 or new_point[1] < 0 or new_point[0] >= H or new_point[1] >= W:
            continue
        
        is_obstacle(point, new_point, direction, obstacles)
        if obstacles and is_obstacle(point, new_point, direction, obstacles):
            continue

        point = new_point

    return point