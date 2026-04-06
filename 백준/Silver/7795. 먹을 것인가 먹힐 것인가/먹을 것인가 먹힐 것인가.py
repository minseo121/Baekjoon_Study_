import sys
input = sys.stdin.readline

t = int(input().strip())

while t:
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0

    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)

    for i in range(n):
        for j in range(m):
            if a[i] > b[j]:
                cnt += m-j
                break
    print(cnt)
    t -= 1