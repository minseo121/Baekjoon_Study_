import sys
input = sys.stdin.readline

c, k = map(int, input().split())
m = 1

m = 10**k

result = c
n = c%m
if n >= (m/2):
    i = m - n
    result += i
elif n < (m/2):
    result -= n

print(result)