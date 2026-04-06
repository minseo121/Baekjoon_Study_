import sys
input = sys.stdin.readline

n = int(input().strip())
al = list(map(int, input().split()))
cnt = 0


while sum(al) != 0:
    al = sorted(al, reverse=True)
    if len(al) > 1 and al[1] > 0:
        al[0] -= 1
        al[1] -= 1
        cnt += 1
    else:
        cnt += al[0]
        al[0] = 0

if cnt > 1440:
    print(-1)
else:
    print(cnt)
