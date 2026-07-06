def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    result = []
    for i in arr1:
        map1.append(bin(i)[2:].zfill(n))
    for i in arr2:
        map2.append(bin(i)[2:].zfill(n))
    
    for i in range(n):
        line=[]
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                line.append('#')
            else:
                line.append(' ')
        result.append(''.join(line))
    
    return result
                
