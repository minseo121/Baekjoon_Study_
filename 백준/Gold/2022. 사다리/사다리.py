import sys
input = sys.stdin.readline

x, y, c = map(float, input().split())

def get_c(mid):
    a = (x**2 - mid**2)**0.5
    b = (y**2 - mid**2)**0.5
    return (a*b)/(a+b)

s, e = 0, min(x,y)
m = 0
while e-s > 0.000001:
    mid = (s+e)/2
    if get_c(mid) >= c:
        s = mid
        m = mid
    elif get_c(mid) <c:
        e = mid

print(f"{m:.3f}")