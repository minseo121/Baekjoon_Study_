from collections import Counter
def solution(weights):
    cnt = Counter(weights)
    #print(cnt)
    ans = 0
    for w in cnt:
        ans += cnt[w] * (cnt[w] - 1) // 2 
        if w*2/3 in cnt:
            ans += cnt[w] * cnt[w*2/3]
        if w*2/4 in cnt:
            ans += cnt[w] * cnt[w*2/4]
        if w*3/4 in cnt:
            ans += cnt[w] * cnt[w*3/4]
    return ans
    
    
    
                
            