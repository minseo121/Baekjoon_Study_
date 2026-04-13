import sys
input = sys.stdin.readline

n,k = map(int, input().split())
li = list(map(int, input().split()))
res = 1000000
idx = []
cnt = 0

for i in range(n):
    if li[i] == 1:
        idx.append(i)
        cnt +=1
if cnt < k:
    print(-1)
else:
    for i in range(cnt-(k-1)):
        res = min(res,(idx[i+(k-1)]-idx[i])+1)

    print(res)

