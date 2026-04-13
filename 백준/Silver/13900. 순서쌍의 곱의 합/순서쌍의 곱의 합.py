import sys
input = sys.stdin.readline

n = int(input().strip())
li = list(map(int, input().split()))
res = 0
num = sum(li)

for i in range(n-1):
    num -= li[i]
    res+=li[i]*(num)

print(res)