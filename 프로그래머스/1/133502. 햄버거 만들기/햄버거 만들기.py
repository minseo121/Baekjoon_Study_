def solution(ingredient):
    ham = [1,2,3,1]
    if len(ingredient) < 4:
        return 0
    else:
        now = ingredient[:3]
        idx = 2
        result = 0
        for i in range(3, len(ingredient)):
            now.append(ingredient[i])
            idx += 1
            if idx >= 3:
                if now[idx-3:idx+1] == ham:
                    now.pop()
                    now.pop()
                    now.pop()
                    now.pop()  
                    result += 1
                    idx -= 4
                
        return result
                
        
        