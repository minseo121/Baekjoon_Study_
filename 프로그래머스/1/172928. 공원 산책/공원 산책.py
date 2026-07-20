def solution(park, routes):
    height = len(park)
    width = len(park[0])
    
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    #북,남,서,동
    
    x, y = 0,0
    for i in range(height):
        for j in range(width):
            if park[i][j] == "S":
                x, y = i, j
    
    for route in routes:
        direction, distance = route.split()
        if direction == 'N':
            dr, dc = directions[0]
        elif direction == 'S':
            dr, dc = directions[1]
        elif direction == 'W':
            dr, dc = directions[2]
        else:
            dr, dc = directions[3]
        
        next_x = x
        next_y = y
        can_move = True
        
        for _ in range(int(distance)):
            next_x += dr
            next_y += dc

            if not (0 <= next_x < height and 0 <= next_y < width):
                can_move = False
                break

            if park[next_x][next_y] == "X":
                can_move = False
                break

        if can_move:
            x, y = next_x, next_y

    return [x, y]