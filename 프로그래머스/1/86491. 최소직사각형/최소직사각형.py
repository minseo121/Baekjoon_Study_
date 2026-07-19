def solution(sizes):
    max_long = 0    
    max_short = 0   
    
    for w, h in sizes:
        long_side = max(w, h)    
        short_side = min(w, h)   
        
        max_long = max(max_long, long_side)
        max_short = max(max_short, short_side)
    
    return max_long * max_short