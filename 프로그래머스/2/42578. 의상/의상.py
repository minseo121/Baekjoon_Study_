def solution(clothes):
    clothes_dict = {}
    answer = 1
    for i in clothes:
        if not i[1] in clothes_dict:
            clothes_dict[i[1]] = []
        clothes_dict[i[1]].append(i[0])
    
    for i in clothes_dict:
        answer *= (len(clothes_dict[i])+1)
    
    return answer-1
    