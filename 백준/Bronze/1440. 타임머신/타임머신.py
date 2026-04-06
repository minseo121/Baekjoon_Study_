import sys
input = sys.stdin.readline

t1, t2, t3 = map(int, input().split(':'))
cnt = 0

if t1 > 59 or t2 > 59 or t3 > 59:
    print(0)
else:
    if t1 <= 12 and t1 >= 1:
        cnt += 2
    if t2 <= 12 and t2 >= 1:
        cnt += 2
    if t3 <= 12 and t3 >= 1:
        cnt += 2

    print(cnt)