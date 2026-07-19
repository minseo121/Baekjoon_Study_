def solution(brown, yellow):
    for yellow_h in range(1, yellow + 1):     
        if yellow % yellow_h != 0:            
            continue
        yellow_w = yellow // yellow_h        
        
        if yellow_w < yellow_h:               
            continue
        
        w = yellow_w + 2
        h = yellow_h + 2
        
        if w * h - yellow == brown:          
            return [w, h]