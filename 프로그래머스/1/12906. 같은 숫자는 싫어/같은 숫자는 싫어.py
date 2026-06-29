def solution(arr):
    result = []
    for i in arr:
        if result and result[-1] == i:
            continue
        else:
            result.append(i)
    return result 