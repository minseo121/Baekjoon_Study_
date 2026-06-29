from collections import defaultdict
def solution(id_list, report, k):
    # 신고한 사람 기준
    user_list = defaultdict(set)
    # 신고당한 사람 기준
    singo_list = defaultdict(set)
    result = []

    for r in report:
        user, singo = r.split(' ')
        user_list[user].add(singo)
        singo_list[singo].add(user)
    
    for id in id_list:
        count = 0
        for singo in user_list[id]:  
            if len(singo_list[singo]) >= k:  
                count += 1
        result.append(count)
    
    return result
            
        