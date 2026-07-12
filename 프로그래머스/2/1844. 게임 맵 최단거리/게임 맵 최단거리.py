from collections import deque
def solution(maps):
    n = len(maps) #행
    m = len(maps[0]) #열
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    
    queue = deque([(0,0,1)])
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x,y,cnt = queue.popleft()
        if x == n-1 and y == m-1:
            return cnt
        else:
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append([nx,ny,cnt+1])
    return -1
        