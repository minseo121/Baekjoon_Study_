from collections import deque
def solution(n, infection, edges, k):
    infection = set([infection])
    graph = [[] for _ in range(n+1)]
    for x, y, pipetype in edges:
        graph[x].append((y, pipetype))
        graph[y].append((x, pipetype)) #양쪽으로
        
    def spread(infected, pipetype):
        new_infected = set(infected)
        queue = deque(infected)
        
        while queue:
            node = queue.popleft()
            for neighbor, edgetype in graph[node]:
                if edgetype == pipetype and neighbor not in new_infected:
                    new_infected.add(neighbor)
                    queue.append(neighbor)
        return new_infected           
    
    def dfs(infected, remaining_k, lasttype):
        if remaining_k == 0:
            return len(infected)
        best = len(infected)
        for pipetype in [1,2,3]:
            if pipetype == lasttype:
                continue
            new_infected = spread(infected, pipetype)
            best = max(best, dfs(new_infected, remaining_k-1, pipetype))
        return best

    return dfs(infection,k,0)
        