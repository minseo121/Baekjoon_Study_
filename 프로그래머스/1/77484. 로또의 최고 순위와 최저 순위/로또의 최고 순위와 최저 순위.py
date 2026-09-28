def solution(lottos, win_nums):
    cnt = 0
    base = 0
    result = []
    for i in range(6):
        if lottos[i] in win_nums:
            base += 1
        else:
            if lottos[i] == 0:
                cnt += 1
    max_result = cnt + base
    min_result = base
    
    if max_result > 1:
        result.append(7-max_result)
    else:
        result.append(6)
    
    if min_result > 1:
        result.append(7-min_result)
    else:
        result.append(6)
    
    return result