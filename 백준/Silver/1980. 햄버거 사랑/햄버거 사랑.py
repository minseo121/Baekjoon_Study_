import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
result = 0
cola = t

for i in range(0, t//n+1):
    time = t
    cnt = 0
    time -= (i*n)
    cnt += time // m
    time -= (cnt * m)
    cnt += i
    if time < cola:
        cola = time
        result = cnt
    elif time == cola:
        if result < cnt:
            result = cnt
            cola = time


print(result, cola)