import sys
input= sys.stdin.readline

a, b = map(int, input().split())
la = set(map(int, input().split()))
lb = set(map(int, input().split()))

ans = la - lb
ans = list(ans)
ans = sorted(ans)
for i in range(len(ans)):
    ans[i] = str(ans[i])
ans = set(ans)

print(len(ans))
if(len(ans)>0):
    print((' ').join(ans))
