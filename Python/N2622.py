import sys
input = sys.stdin.readline

n = int(input().strip())
if n == 1 or n == 2 or n==4:
    print(0)
else:
    num = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            k = n - (i+j)
            if k >= (i+j):
                continue
            else:
                if j > k:
                    break
                num += 1
    print(num)

    