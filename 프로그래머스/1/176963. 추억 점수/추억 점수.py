def solution(name, yearning, photo):
    mem = dict()
    result = [0] * (len(photo))
    idx = 0
    for i in range(len(name)):
        mem[name[i]] = yearning[i]
        
    for i in photo:
        for j in i:
            result[idx] += mem.get(j,0) 
        idx += 1
    return result