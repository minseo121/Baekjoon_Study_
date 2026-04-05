import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listen = set([input().strip() for _ in range(n)])
see = set([input().strip() for _ in range(m)])

result = sorted(list(listen&see))
print(len(result))
[print(i) for i in result]

