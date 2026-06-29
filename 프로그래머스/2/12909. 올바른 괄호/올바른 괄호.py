def solution(s):
    result = []
    for i in s:
        if i == ')':
            if result and result[-1] == '(':
                result.pop()
            else:
                result.append(i)
        else:
            result.append(i)
    
    if result:
        return False
    else:
        return True
            