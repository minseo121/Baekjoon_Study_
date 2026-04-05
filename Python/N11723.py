import sys
input = sys.stdin.readline

m = int(input().strip())
s = set([])

for _ in range(m):
    say = input().split()
    order = say[0]
    if len(say) > 1 :
        num = int(say[1])
    if order == "add":
        s.add(num)
    elif order == "remove":
        s.discard(num)
    elif order == "check":
        if num in s:
            print(1)
        else:
            print(0)
    elif order == "toggle" :
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif order == "all":
        s=set(range(1,21))
    elif order == "empty":
        s.clear()