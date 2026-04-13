import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = []
for i in range(N):
    li.append(int(input().strip()))

s, e = 0, sum(li)
can = e

while s <= e:
    mid = (s+e)//2
    cnt = 1 #처음 인출
    money = mid
    for i in li:
        if money < i:
            if mid < i: #애초에 그냥 mid가 i가 안될때는 방법이 없으므로 s를 mid+1로 이동해야함.
                cnt = M+1
                break
            else:
                cnt += 1
                money = mid
        money -= i
    if cnt > M:
        s = mid+1
    else:
        can = mid
        e = mid-1
print(can)
