import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
j = m

for _ in range(n):
    a, b = map(int, input().split())

    m = (m+a)-b
    if m > j:
        j = m
    if m < 0:
        print(0)
        break
if not m <0:
    print(j)