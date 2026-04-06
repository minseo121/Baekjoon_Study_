import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))
high = 0
start = nums[0]
result = 0

for i in range(1,n):
    if nums[i] > nums[i-1]:
        high = nums[i]
        if result < (high-start):
            result = high - start
    elif nums[i] <= nums[i-1]:
        start = nums[i]
print(result)