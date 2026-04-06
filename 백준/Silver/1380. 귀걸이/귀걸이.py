import sys
input = sys.stdin.readline

cnt = 1

while True:
    n = int(input().strip())
    if n == 0:
        break
    else:
        name = []
        found = [0]*(2*n-1) #잃어버리면 1, 찾으면 0
        for _ in range(n):
            name.append(input().strip())
        for _ in range(2*n-1):
            member = (input().split())
            num = int(member[0])
            if found[num-1] == 0:
                found[num-1] = 1
            else:
                found[num-1] = 0
        id = found.index(1)
        print(cnt, name[id])
        cnt += 1
