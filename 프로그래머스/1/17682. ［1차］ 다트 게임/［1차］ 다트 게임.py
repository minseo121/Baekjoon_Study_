def solution(dartResult):
    dartResult = list(dartResult)
    first = []
    for i in range(len(dartResult)):
        if dartResult[i] in ('S', 'D', 'T'):
            # 10 체크
            if i >= 2 and dartResult[i-2].isdigit():
                num = int(dartResult[i-2] + dartResult[i-1])
            else:
                num = int(dartResult[i-1])

            if dartResult[i] == 'S':
                first.append(num)
            elif dartResult[i] == 'D':
                first.append(num ** 2)
            elif dartResult[i] == 'T':
                first.append(num ** 3)
        elif dartResult[i] == '*':
            first.append('*')
        elif dartResult[i] == '#':
            first.append('#')
    print('첫번째', first)
    
    second = []
    for i in range(len(first)):
        if first[i] == '*':
            if i >= 2:
                second[-2] *= 2
                second[-1] *= 2
            else:
                second[-1] *= 2
        elif first[i] == '#':
            second[-1]*= (-1)
        else:
            second.append(first[i])

    print('두번째', second)
    answer = 0
    for i in second:
        answer += i
    
    return answer