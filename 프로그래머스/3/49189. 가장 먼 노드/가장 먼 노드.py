from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    dist = [-1] * (n+1)
    dist[1] = 0
    q = deque([1])
    
    while q:
        current = q.popleft()
        for n in graph[current]:
            if dist[n] == -1:
                dist[n] = dist[current] + 1
                q.append(n)
    max_dist = max(dist[1:])
    return dist[1:].count(max_dist)