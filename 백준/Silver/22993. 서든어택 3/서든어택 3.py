import sys
input = sys.stdin.readline

n = int(input().strip())
num = list(map(int, input().split()))

jun = num[0]
others = sorted(num[1:])

for i in others:
    if jun > i:
        jun += i
    else:
        print('No')
        break
else:
    print('Yes')

