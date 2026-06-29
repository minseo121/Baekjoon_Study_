from collections import deque
def solution(priorities, location):
    answer = []
    process = deque()
    prior = deque(priorities)
    for i in range(len(priorities)):
        process.append(i)
    found = process[location]
    
    
    while process:
        up = False
        pro = process.popleft()
        num = prior.popleft()
        for i in prior:
            if num < i:
                up = True
        if up:
            process.append(pro)
            prior.append(num)
        else:
            answer.append(pro)
    return (answer.index(found)+1)
        
    