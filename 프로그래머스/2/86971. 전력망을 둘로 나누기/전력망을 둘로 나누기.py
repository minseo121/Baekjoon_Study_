from collections import deque

def solution(n, wires):
    answer = n   
    
    for i in range(len(wires)):
        graph = {node: [] for node in range(1, n + 1)}
        for j in range(len(wires)):
            if i == j:            
                continue
            a, b = wires[j]
            graph[a].append(b)    
            graph[b].append(a)
        
        cnt = bfs(graph, n)
        
        diff = abs(cnt - (n - cnt))
        answer = min(answer, diff)
    
    return answer

def bfs(graph, n):
    start = 1
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1                    
    
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                count += 1
                queue.append(next_node)
    
    return count