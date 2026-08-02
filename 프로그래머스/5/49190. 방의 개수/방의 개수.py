def solution(arrows):
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]
    
    x,y = 0,0
    visited_node = {(0,0)}
    visited_edge = set()
    answer = 0
    
    for a in arrows:
        for _ in range(2):
            nx, ny = x + dx[a], y+dy[a]
            if (nx, ny) in visited_node and ((x,y),(nx,ny))not in visited_edge:
                answer += 1
            visited_edge.add(((x,y),(nx,ny)))
            visited_edge.add(((nx,ny),(x,y)))
            visited_node.add((nx,ny))
            x, y = nx, ny
    return answer