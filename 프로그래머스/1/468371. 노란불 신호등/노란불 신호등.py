import math
def solution(signals):
    time = 1
    for g,y,r in signals:
        total = g+y+r
        time = time*total//math.gcd(time,total)
    
    for i in range(1, time+1):
        all_yellow = True
        for g,y,r in signals:
            total = g+y+r
            idx = i%total
            if not (idx <= g+y and idx > g):
                all_yellow = False
                break
        if all_yellow:
            return i
    return -1
    
    
        
            
        
        
        