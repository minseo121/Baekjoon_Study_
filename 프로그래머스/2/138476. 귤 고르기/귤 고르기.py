from collections import defaultdict
def solution(k, tangerine):
    size = defaultdict(int)
    for i in tangerine:
        size[i] += 1
    
    sorted_items = sorted(size.items(), key=lambda x:x[1], reverse=True)
    cnt = 0
    answer = 0
    for i in sorted_items:
        cnt += i[1]
        answer += 1
        if cnt >= k:
            break
    return answer