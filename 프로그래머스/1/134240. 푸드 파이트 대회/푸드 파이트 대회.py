from collections import deque

def solution(food):
    result = []
    first = deque()
    for i in range(1, len(food)):
        cnt = int(food[i])//2
        for _ in range(cnt):
            first.append(i)

    for _ in range(len(first)):
        num = first.popleft()
        result.append(num)
        first.append(num)
    result.append(0)
    for _ in range(len(first)):
        result.append(first.pop())
    return ''.join(map(str, result))