from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    answer = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'X' or visited[i][j]:
                continue

            queue = deque([(i, j)])
            visited[i][j] = True
            total = 0

            while queue:
                x, y = queue.popleft()
                total += int(maps[x][y])

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < m:
                        if maps[nx][ny] != 'X' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

            answer.append(total)
    if answer:
        return sorted(answer) 
    else:
        return [-1]