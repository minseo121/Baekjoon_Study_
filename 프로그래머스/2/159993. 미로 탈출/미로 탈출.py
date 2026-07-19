from collections import deque

def bfs(maps, start, end):
    n = len(maps)          
    m = len(maps[0])       
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                sx, sy = i, j
            if maps[i][j] == end:
                ex, ey = i, j
    
    visited = [[-1] * m for _ in range(n)]
    
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = 0   
    
    while queue:
        x, y = queue.popleft()
        
        if x == ex and y == ey:   # 도착
            return visited[x][y]
        
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 'X':
                continue
            if visited[nx][ny] != -1:
                continue
            
            visited[nx][ny] = visited[x][y] + 1  
            queue.append((nx, ny))
    
    return -1   

def solution(maps):
    to_lever = bfs(maps, 'S', 'L')
    to_exit = bfs(maps, 'L', 'E')
    
    if to_lever == -1 or to_exit == -1:
        return -1
    
    return to_lever + to_exit