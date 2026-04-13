import sys
input=sys.stdin.readline

n = int(input().strip())
li = list(map(int, input().split()))
res = 0

li.sort()

for i in range(n-1):
    s = i+1
    e = n-1
    cnt = 0
    while s <= e:
        m = (s+e)//2
        if li[i] >= 0.9*li[m]:
            cnt = m
            s = m+1
        else:
            e = m-1
    if cnt > 0:
        res += cnt - i
    else:
        res += 0

print(res)