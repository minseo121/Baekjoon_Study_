import sys
input = sys.stdin.readline

n = int(input().strip())
nums=[0]*(n+1)
nums[0] = 0
if n > 0:
    nums[1] = 1

for i in range(2, n+1):
    nums[i] = nums[i-1] + nums[i-2]

print(nums[n])