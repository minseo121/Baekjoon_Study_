from collections import deque
def solution(prices):
    result = []
    deq = deque(prices)
    for i in range(len(prices)):
        num = deq.popleft()
        cnt = 0
        for i in deq:
            cnt +=1
            if i < num:
                break
        result.append(cnt)
    return result
            