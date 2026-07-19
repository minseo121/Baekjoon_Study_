def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)   
    
    def explore(fatigue, count):
        nonlocal answer
        answer = max(answer, count)     
        
        for i in range(len(dungeons)):
            need, use = dungeons[i]
            if not visited[i] and fatigue >= need:
                visited[i] = True                    
                explore(fatigue - use, count + 1)    
                visited[i] = False                  
    
    explore(k, 0)
    return answer