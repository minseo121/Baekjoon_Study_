def solution(n, words):
    result = []
    
    for i in range(1,len(words)):
        if words[i] in words[:i] or words[i-1][-1] != words[i][0]:
            result.append(i%n+1)
            result.append(i//n+1)
            break
        
    if not result:
        return [0,0]
    
    return result