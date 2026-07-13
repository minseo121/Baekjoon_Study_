def solution(keymap, targets):
    result = []
    for target in targets:
        ans = 0
        possible = True
        for t in target:
            min_num = 101         
            for key in keymap:
                if t in key:
                    idx = key.index(t) + 1
                    if idx < min_num:
                        min_num = idx
            if min_num == 101:     
                possible = False
                break
            ans += min_num
        if possible:
            result.append(ans)
        else:
            result.append(-1)
    return result