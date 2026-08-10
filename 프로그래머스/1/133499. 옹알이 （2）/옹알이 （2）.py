def solution(babbling):
    cnt = 0
    for s in babbling:
        l = len(s)
        j = 0
        prev = -1
        can = True
        while j < l:
            if prev != 0 and s[j:j+3] == "aya":
                prev, j = 0, j + 3
            elif prev != 1 and s[j:j+2] == "ye":
                prev, j = 1, j + 2
            elif prev != 2 and s[j:j+3] == "woo":
                prev, j = 2, j + 3
            elif prev != 3 and s[j:j+2] == "ma":
                prev, j = 3, j + 2
            else:
                can = False
                break
        if can:
            cnt += 1
    return cnt