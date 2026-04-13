import sys
from collections import defaultdict
input = sys.stdin.readline

r, c = map(int, input().split())
li = []
for _ in range(r):
    li.append(input().strip())

s, e = 0, r-1
cnt = 0

while s<=e:
    mid = (s+e)//2
    check = True
    dict = defaultdict(int)
    for i in range(c):
        text = ''
        for j in range(mid, r):
            text += li[j][i]
        if not dict[text]:
            dict[text] += 1
        else:
            check = False
            break
    if not check:
        e = mid-1
    else:
        s = mid+1
        cnt = mid

print(cnt)